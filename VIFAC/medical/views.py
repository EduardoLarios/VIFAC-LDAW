from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import UpdateView
from django.urls import reverse_lazy, reverse
from .forms import MedicoForm, RegistroForm, LaboratorioForm, UltrasonidoForm, ProblemasForm
from .models import Exp_Medico
from django.views.generic import UpdateView

def index(request):
    query = Exp_Medico.objects.all()
    if query:
        context = {
            'expedientes': query
        }
    else:
        res = True
        context = {
            'no_results': res
        }
    return render(request, 'medical/index.html', context)
    return render(request, 'medical/index.html')

def file_detail(request, file_id):
    file = get_object_or_404(Exp_Medico, pk=file_id)
    registros = file.registro_set.all()
    labs = file.laboratorio_set.all()
    us = file.ultrasonido_set.all()
    problemas = file.problemas_set.all()
    context = {
        'file': file,
        'registros': registros,
        'labs': labs,
        'us': us,
        'problemas': problemas,
    }
    return render(request, 'medical/file_detail.html', context)

class FileEdit(UpdateView):

    model = Exp_Medico
    fields = [
        'nombre',
        'tipo_sanguineo',
        'edad',
        'fecha_nacimiento',
        'estado_civil',
        'telefono',
        'domicilio',
        'padre_bebe',
        'edad_padre',
        'apoyo',
        'FUM',
        'ciclos',
        'uso_anticonceptivos_FUM',
        'fppxfum',
        'fppxusg',
        'fpp_definitiva',
        'G',
        'P',
        'termino',
        'Ab',
        'ectop',
        'multiples',
        'cesarea',
        'medicamento_desde_fum',
        'contacto_con_enfermedad_infecciosa_fum',
        'embarazos_anteriores',
        'app',
        'medicamentos',
        'cirugias',
        'alergias',
        'apnp_fuma',
        'alcohol',
        'droga',
        'trabajo',
        'ahf',
        'ahf_padre',
    ]
    template_name = "medical/new_file.html"
    success_url = reverse_lazy('medical:index')

def new_lab(request, file_id):
    form = LaboratorioForm(request.POST or None)
    file = get_object_or_404(Participante, pk=file_id)
    if form.is_valid():
        lab = form.save(commit=False)
        lab.participante = file
        lab.save()

        if '_addother' in request.POST:
            form = AsignPanfletForm()
            context = {
                'participante': part,
                'panfleta': panfleta,
                'form': form,
            }
            return render(request, 'raffles/new_raffle.html', context)
        else:
            return HttpResponseRedirect(reverse('raffles:panfletas_part', args=(part.id,)))
        # return render(request, 'raffles/index.html', {'album': album})

    context = {
        'participante': part,
        'form': form,
    }
    return render(request, 'raffles/new_raffle.html', context)


def new_ultrasonido(request):
    context = {}
    if request.method == "POST":

        # Get the form through POST
        new_record_form = MedicoForm(request.POST)

        # Validate form data
        if new_record_form.is_valid():
            # Get form variables
            # Create donor object
            context['record'] = Exp_Medico.objects.create(**new_record_form.cleaned_data)
            return list_record(request)

        context['form'] = new_record_form
        return render(request, 'medical/new_record.html', context)

    else:
        new_file_form = MedicoForm()

    context['form'] = new_file_form

    return render(request, 'medical/new_record.html', context)


def new_file(request):
    if request.method == "POST":
        # Get the form through POST
        new_file_form = MedicoForm(request.POST or None)
        
        # Validate form data
        if new_file_form.is_valid():
            # Get form variables
            # Create donor object
            exp = Exp_Medico.objects.create(**new_file_form.cleaned_data)
            return reverse_lazy('medical:index')

        context = {
            'form': new_file_form,
        }
        return render(request, 'medical/new_file.html', context)
    
    else:
        new_record_form = MedicoForm()
    
    context = {
        'form': new_record_form
    }
    return render(request, 'medical/new_file.html', context)


def RecordDelete(request, pk):
    model = get_object_or_404(Exp_Medico, pk=pk)
    # noinspection PyArgumentList
    model.delete()
    return HttpResponseRedirect(reverse('medical:list_records'))