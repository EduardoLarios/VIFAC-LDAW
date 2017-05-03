from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, ListView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import Http404
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
import datetime
import csv
import os

from rolepermissions.checkers import has_role
from .forms import RecordForm, DocumentForm
from .models import Expediente, Documento


# Create your views here.

def index(request):
    if has_role(request.user, ['expedientes', 'admin']):
        context = {}
        return render(request, 'records/index.html', context)
    else:
        raise Http404
    
# Search View
class RecordSearchListView(ListView):
    """
    Display a Record List page filtered by the search query.
    """
    
    template_name = 'records/list_records.html'
    model = Expediente
    paginate_by = 20

    def get_queryset(self):
        
        result = self.model.objects.all()
        query = self.request.GET.get('q', None)
        
        if query is not None and query:
            
            result = result.filter(Q(nombre__icontains = query) | Q(apellido_paterno__icontains = query) | Q(apellido_materno__icontains = query))
            result = result.order_by('apellido_paterno', 'apellido_materno', 'nombre')

        return result

# Detail View

class RecordDetailView(UpdateView):
    model = Expediente
    fields = [
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'edad',
        'telefono_casa',
        'telefono_particular',
        'estado_nacimiento',
        'fecha_nacimiento',
        'religion',
        'tipo_poblacion',
        'migrante',
        'estado',
        'estado_civil',
        'ciudad',
        'calle',
        'colonia',
        'codigo_postal',
        'vives_nombre',
        'vives_apellido_paterno',
        'vives_apellido_materno',
        'tipo_relacion_vives',
        'telefono_vives',
        'estado_vives',
        'ciudad_vives',
        'calle_vives',
        'codigo_postal_vives',
        'colonia_vives',
        'vive_padre',
        'padre_nombre',
        'padre_apellido_paterno',
        'padre_apellido_materno',
        'padre_telefono_casa',
        'padre_telefono_particular',
        'padre_fecha_nacimiento',
        'padre_estado_civil',
        'padre_ocupacion',
        'padre_estado',
        'padre_ciudad',
        'padre_calle',
        'padre_codigo_postal',
        'padre_colonia',
        'vive_madre',
        'madre_nombre',
        'madre_apellido_paterno',
        'madre_apellido_materno',
        'madre_telefono_casa',
        'madre_telefono_particular',
        'madre_fecha_nacimiento',
        'madre_estado_civil',
        'madre_migrante',
        'madre_estado',
        'madre_ciudad',
        'madre_calle',
        'madre_colonia',
        'madre_ocupacion',
        'madre_codigo_postal',
        'integrantes_familia',
        'numero_hermanos',
        'lugar_dentro_familia',
        'relacion_padre',
        'relacion_madre',
        'relacion_hermanos',
        'encargado_crianza',
        'trabajado_antes',
        'puesto',
        'lugar_trabajo',
        'jefe_inmediato',
        'telefono_jefe',
        'trabajo_estado',
        'trabajo_ciudad',
        'trabajo_calle',
        'trabajo_colonia',
        'trabajo_codigo_postal',
        'referencia',
        'visto_en',
        'canal',
        'otros',
        'nombre_recomendacion',
        'apellido_paterno_recomendacion',
        'apellido_materno_recomendacion',
        'relacion_recomendacion',
        'calle_recomendacion',
        'telefono_recomendacion',
        'numero_exterior',
        'codigo_postal_recomendacion',
        'colonia',
        'ciudad_referencia',
        'estado_referencia',
        'tipo_de_ayuda',
        'fecha_ultima_menstruacion',
        'fecha_de_parto_esperada',
        'nombre_emergencia',
        'apellido_paterno_emergencia',
        'apellido_materno_emergencia',
        'relacion_emergencia',
        'codigo_postal_emergencia',
        'telefono_emergencia',
        'calle_emergencia',
        'colonia_emergencia',
        'ciudad_emergencia',
        'estado_emergencia',
        'control_medico',
        'enfermedades_padecidas',
        'nombre_medico',
        'nombre_clinica',
        'telefono_medico',
        'calle_medico',
        'numero_exterior_medico',
        'codigo_postal_medico',
        'colonia_medico',
        'ciudad_medico',
        'estado_medico',
        'estado_de_animo',
        'infancia',
        'tipo_embarazo',
        'reaccion',
        'apoyo_papa',
        'relacion_con_padre',
        'duracion_relacion',
        'familiares',
        'actitud_familiares',
        'relacion_voluntaria',
        'comunicacion_padre',
        'aborto_considerado',
        'violencia_intrafamiliar',
        'maximo_grado_estudios',
        'primaria_nombre',
        'primaria_tiempo',
        'secundaria_nombre',
        'secundaria_tiempo',
        'preparatoria_nombre',
        'preparatoria_tiempo',
        'tecnica_nombre',
        'tecnica_tiempo',
        'licenciatura_nombre',
        'licenciatura_tiempo',
        'posgrado_nombre',
        'posgrado_tiempo',
        'otro_nombre',
        'otro_tiempo',
    ]
    template_name = 'records/expediente_detail.html'
    success_url = '/expedientes/lista_expedientes/'

# Export to CSV

def export_records_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="records.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['Expediente N°',
         'Nombre',
         'Apellido Paterno',
         'Apellido Materno',
         'Edad',
         'Teléfono de Casa',
         'Teléfono Particular',
         'Estado de Nacimiento',
         'Fecha de Nacimiento',
         'Estado Civil',
         'Religión',
         'Tipo de Población',
         'Migrante',
         'Estado',
         'Ciudad',
         'Colonia',
         'Calle',
         'Código Postal',
         'Fecha de Ingreso'
         ]
    )

    records = Expediente.objects.all().values_list(
       'id',
       'nombre',
       'apellido_paterno',
       'apellido_materno',
       'edad',
       'telefono_casa',
       'telefono_particular',
       'estado_nacimiento',
       'fecha_nacimiento',
       'estado_civil',
       'religion',
       'tipo_poblacion',
       'migrante',
       'estado',
       'ciudad',
       'colonia',
       'calle',
       'codigo_postal',
       'fecha_ingreso'
    )
    
    for record in records:
        writer.writerow(record)

    return response

# New DB entries

def new_record(request):
    if has_role(request.user, ['expedientes', 'admin']):
        context = {'today': datetime.datetime.now()}
        
        if request.method == "POST":
            
            # Get the form through POST
            new_record_form = RecordForm(request.POST)
            
            # Validate form data
            if new_record_form.is_valid():
                # Get form variables
                # Create donor object
                context['record'] = Expediente.objects.create(**new_record_form.cleaned_data)
                return list_record(request)
            
            context['form'] = new_record_form
            return render(request, 'records/new_record.html', context)
        
        else:
            new_record_form = RecordForm()
        
        context['form'] = new_record_form
        
        return render(request, 'records/new_record.html', context)
    else:
        raise Http404

# List all records
class RecordListView(ListView):
    """
    Display a Record List page filtered by the search query.
    """
    
    template_name = 'records/list_records.html'
    model = Expediente
    paginate_by = 20

list_record = RecordListView.as_view()

#Delete from DB

def RecordDelete(request, pk):
    if has_role(request.user, ['expedientes', 'admin']):
        model = get_object_or_404(Expediente, pk=pk)
        # noinspection PyArgumentList
        model.delete()
        return HttpResponseRedirect(reverse('records:list_records'))
    else:
        raise Http404

class RecordUpdate(UpdateView):
    model = Expediente
    fields = [
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'edad',
        'telefono_casa',
        'telefono_particular',
        'estado_nacimiento',
        'fecha_nacimiento',
        'religion',
        'tipo_poblacion',
        'migrante',
        'estado',
        'estado_civil',
        'ciudad',
        'calle',
        'colonia',
        'codigo_postal',
        'vives_nombre',
        'vives_apellido_paterno',
        'vives_apellido_materno',
        'tipo_relacion_vives',
        'telefono_vives',
        'estado_vives',
        'ciudad_vives',
        'calle_vives',
        'codigo_postal_vives',
        'colonia_vives',
        'vive_padre',
        'padre_nombre',
        'padre_apellido_paterno',
        'padre_apellido_materno',
        'padre_telefono_casa',
        'padre_telefono_particular',
        'padre_fecha_nacimiento',
        'padre_estado_civil',
        'padre_ocupacion',
        'padre_estado',
        'padre_ciudad',
        'padre_calle',
        'padre_codigo_postal',
        'padre_colonia',
        'vive_madre',
        'madre_nombre',
        'madre_apellido_paterno',
        'madre_apellido_materno',
        'madre_telefono_casa',
        'madre_telefono_particular',
        'madre_fecha_nacimiento',
        'madre_estado_civil',
        'madre_migrante',
        'madre_estado',
        'madre_ciudad',
        'madre_calle',
        'madre_colonia',
        'madre_ocupacion',
        'madre_codigo_postal',
        'integrantes_familia',
        'numero_hermanos',
        'lugar_dentro_familia',
        'relacion_padre',
        'relacion_madre',
        'relacion_hermanos',
        'encargado_crianza',
        'trabajado_antes',
        'puesto',
        'lugar_trabajo',
        'jefe_inmediato',
        'telefono_jefe',
        'trabajo_estado',
        'trabajo_ciudad',
        'trabajo_calle',
        'trabajo_colonia',
        'trabajo_codigo_postal',
        'referencia',
        'visto_en',
        'canal',
        'otros',
        'nombre_recomendacion',
        'apellido_paterno_recomendacion',
        'apellido_materno_recomendacion',
        'relacion_recomendacion',
        'calle_recomendacion',
        'telefono_recomendacion',
        'numero_exterior',
        'codigo_postal_recomendacion',
        'colonia',
        'ciudad_referencia',
        'estado_referencia',
        'tipo_de_ayuda',
        'fecha_ultima_menstruacion',
        'fecha_de_parto_esperada',
        'nombre_emergencia',
        'apellido_paterno_emergencia',
        'apellido_materno_emergencia',
        'relacion_emergencia',
        'codigo_postal_emergencia',
        'telefono_emergencia',
        'calle_emergencia',
        'colonia_emergencia',
        'ciudad_emergencia',
        'estado_emergencia',
        'control_medico',
        'enfermedades_padecidas',
        'nombre_medico',
        'nombre_clinica',
        'telefono_medico',
        'calle_medico',
        'numero_exterior_medico',
        'codigo_postal_medico',
        'colonia_medico',
        'ciudad_medico',
        'estado_medico',
        'estado_de_animo',
        'infancia',
        'tipo_embarazo',
        'reaccion',
        'apoyo_papa',
        'relacion_con_padre',
        'duracion_relacion',
        'familiares',
        'actitud_familiares',
        'relacion_voluntaria',
        'comunicacion_padre',
        'aborto_considerado',
        'violencia_intrafamiliar',
        'maximo_grado_estudios',
        'primaria_nombre',
        'primaria_tiempo',
        'secundaria_nombre',
        'secundaria_tiempo',
        'preparatoria_nombre',
        'preparatoria_tiempo',
        'tecnica_nombre',
        'tecnica_tiempo',
        'licenciatura_nombre',
        'licenciatura_tiempo',
        'posgrado_nombre',
        'posgrado_tiempo',
        'otro_nombre',
        'otro_tiempo',
    ]
    template_name = 'records/record_edit_form.html'
    success_url = '/expedientes/lista_expedientes/'


def model_form_upload(request, exp_id):
    if has_role(request.user, ['expedientes', 'admin']):
        exp = get_object_or_404(Expediente, pk=exp_id)
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                documento = form.save(commit=False)
                documento.expediente = exp
                documento.save()
                return HttpResponseRedirect(reverse('records:list_records'))
        else:
            form = DocumentForm()
        return render(request, 'records/model_form_upload.html', {
            'form': form,
            'expediente': exp
        })
    else:
        raise Http404


def list_documents(request, exp_id):
    if has_role(request.user, ['expedientes', 'admin']):
        expediente = get_object_or_404(Expediente, pk=exp_id)
        documentos = expediente.documento_set.all()
        context = {
            'expediente': expediente,
            'documentos': documentos,
        }
        return render(request, 'records/document_list.html', context)
    else:
        raise Http404


def download(request, path):
    if has_role(request.user, ['expedientes', 'admin']):
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        else:
            raise Http404
    else:
        raise Http404


def delete_document(request, doc_id):
    if has_role(request.user, ['expedientes', 'admin']):
        document = Documento.objects.get(pk=doc_id)
        document.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        raise Http404
