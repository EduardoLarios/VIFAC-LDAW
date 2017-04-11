from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import datetime

from VIFAC.records.models import Expediente
from .forms import RecordForm

# Create your views here.

def index(request):
    context = {}
    return render(request, 'records/index.html', context)


# New DB entries

def new_record(request):
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

# List all records

def list_record(request):
    records = Expediente.objects.all().values()

    return render(request, 'records/list_records.html', {'records': records})

#Delete from DB

def RecordDelete(request, pk):
    model = get_object_or_404(Expediente, pk=pk)
    # noinspection PyArgumentList
    model.delete()
    return HttpResponseRedirect(reverse('records:list_records'))

class RecordUpdate(UpdateView):
    model = Expediente
    form_class = RecordForm
    template_name = 'records/record_edit_form.html'
    slug_field = 'full_name'
    slug_url_kwarg = 'slug'
    success_url = '/donaciones/list_records'
