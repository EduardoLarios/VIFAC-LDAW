from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import UpdateView
from django.urls import reverse_lazy, reverse
from .forms import MedicoForm
from .models import Exp_Medico


def index(request):
    return render(request, 'medical/index.html')


def new_laboratorio(request):
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
        new_record_form = MedicoForm()

    context['form'] = new_record_form

    return render(request, 'medical/new_record.html', context)


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
        new_record_form = MedicoForm()

    context['form'] = new_record_form

    return render(request, 'medical/new_record.html', context)


def new_record(request):
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
        new_record_form = MedicoForm()
    
    context['form'] = new_record_form
    
    return render(request, 'medical/new_record.html', context)


def list_record(request):
    records = Exp_Medico.objects.all()

    return render(request, 'medical/list_records.html', {'records': records})


def RecordDelete(request, pk):
    model = get_object_or_404(Exp_Medico, pk=pk)
    # noinspection PyArgumentList
    model.delete()
    return HttpResponseRedirect(reverse('medical:list_records'))