from .forms import MedicoForm, RegistroForm, LaboratorioForm, UltrasonidoForm, ProblemasForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView
from .models import Exp_Medico, Laboratorio, Ultrasonido, Problemas, Registro

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

def file_delete(request, file_id):
    file = Exp_Medico.objects.get(pk=file_id)
    file.delete()
    return HttpResponseRedirect(reverse('medical:index'))

def new_file(request):
    if request.method == "POST":
        # Get the form through POST
        new_file_form = MedicoForm(request.POST)

        # Validate form data
        if new_file_form.is_valid():
            # Get form variables
            # Create donor object
            exp = Exp_Medico.objects.create(**new_file_form.cleaned_data)
            return HttpResponseRedirect(reverse('medical:index'))

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
    template_name = "medical/edit_file.html"
    success_url = '/expediente_medico/'

def file_delete(request, file_id):
    file = Exp_Medico.objects.get(pk=file_id)
    file.delete()
    redirect_url = reverse('medical:index')
    extra_params = ''
    full_redirect_url = '%s%s' % (redirect_url, extra_params)
    return HttpResponseRedirect(full_redirect_url)

def new_registro(request, file_id):
    form = RegistroForm(request.POST or None)
    file = get_object_or_404(Exp_Medico, pk=file_id)
    if form.is_valid():
        registro = form.save(commit=False)
        registro.paciente = file
        registro.save()

        return HttpResponseRedirect(reverse('medical:file_detail', args=(file_id,)))

    context = {
        'form': form,
    }
    return render(request, 'medical/new_registro.html', context)

def edit_registro(request, registro_id):
    registro = get_object_or_404(Registro, pk = registro_id)
    form = RegistroForm(instance = registro)
    file = registro.paciente
    if request.method == "POST":
        form = RegistroForm(request.POST, instance = registro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('medical:file_detail', args = (file.id,)))

    context = {
        'form': form,
        'registro': registro
    }
    return render(request, 'medical/edit_registro.html', context)

def registro_delete(request, registro_id):
    registro = Registro.objects.get(pk=registro_id)
    file = registro.paciente
    registro.delete()
    redirect_url = reverse('medical:file_detail', args = (file.id,))
    extra_params = '#registro'
    full_redirect_url = '%s%s' % (redirect_url, extra_params)
    return HttpResponseRedirect(full_redirect_url)

def new_lab(request, file_id):
    form = LaboratorioForm(request.POST or None)
    file = get_object_or_404(Exp_Medico, pk=file_id)
    if form.is_valid():
        lab = form.save(commit=False)
        lab.paciente = file
        lab.save()

        return HttpResponseRedirect(reverse('medical:file_detail', args=(file_id,)))
        # return render(request, 'raffles/index.html', {'album': album})

    context = {
        'form': form,
    }
    return render(request, 'medical/new_lab.html', context)

def edit_lab(request, lab_id):
    lab = get_object_or_404(Laboratorio, pk = lab_id)
    form = LaboratorioForm(instance = lab)
    file = lab.paciente
    if request.method == "POST":
        form = LaboratorioForm(request.POST, instance = lab)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('medical:file_detail', args = (file.id,)))

    context = {
        'form': form,
        'lab': lab
    }
    return render(request, 'medical/edit_lab.html', context)


def lab_delete(request, lab_id):
    lab = Laboratorio.objects.get(pk=lab_id)
    file = lab.paciente
    lab.delete()
    redirect_url = reverse('medical:file_detail', args = (file.id,))
    extra_params = '#laboratorios'
    full_redirect_url = '%s%s' % (redirect_url, extra_params)
    return HttpResponseRedirect(full_redirect_url)

def new_ultrasonido(request, file_id):
    form = UltrasonidoForm(request.POST or None)
    file = get_object_or_404(Exp_Medico, pk = file_id)
    if form.is_valid():
        us = form.save(commit = False)
        us.paciente = file
        us.save()

        return HttpResponseRedirect(reverse('medical:file_detail', args = (file_id,)))

    context = {
        'form': form,
    }
    return render(request, 'medical/new_us.html', context)

def edit_us(request, us_id):
    us = get_object_or_404(Ultrasonido, pk = us_id)
    form = UltrasonidoForm(instance = us)
    file = us.paciente
    if request.method == "POST":
        form = LaboratorioForm(request.POST, instance = us)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('medical:file_detail', args = (file.id,)))

    context = {
        'form': form,
        'us': us
    }
    return render(request, 'medical/edit_lab.html', context)

def us_delete(request, us_id):
    us = Ultrasonido.objects.get(pk=us_id)
    file = us.paciente
    us.delete()
    redirect_url = reverse('medical:file_detail', args = (file.id,))
    extra_params = '#ultrasonidos'
    full_redirect_url = '%s%s' % (redirect_url, extra_params)
    return HttpResponseRedirect(full_redirect_url)

def new_problema(request, file_id):
    form = ProblemasForm(request.POST or None)
    file = get_object_or_404(Exp_Medico, pk = file_id)
    if form.is_valid():
        problema = form.save(commit = False)
        problema.paciente = file
        problema.save()

        return HttpResponseRedirect(reverse('medical:file_detail', args = (file_id,)))

    context = {
        'form': form,
    }
    return render(request, 'medical/new_problema.html', context)

def edit_problem(request, problema_id):
    problema = get_object_or_404(Problemas, pk = problema_id)
    form = ProblemasForm(instance = problema)
    file = problema.paciente
    if request.method == "POST":
        form = ProblemasForm(request.POST, instance = problema)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('medical:file_detail', args = (file.id,)))

    context = {
        'form': form,
        'problema': problema
    }
    return render(request, 'medical/edit_problema.html', context)

def problema_delete(request, problema_id):
    problema = Problemas.objects.get(pk=problema_id)
    file = problema.paciente
    problema.delete()
    redirect_url = reverse('medical:file_detail', args = (file.id,))
    extra_params = '#problemas'
    full_redirect_url = '%s%s' % (redirect_url, extra_params)
    return HttpResponseRedirect(full_redirect_url)