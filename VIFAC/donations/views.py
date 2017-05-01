from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.urls import reverse
import datetime
import logging
from rolepermissions.checkers import has_role
from django.http import Http404

from .forms.categories import CategoriesForm
from .forms.donations import DonationForm
from .forms.donors import DonorForm

from .models.categories import Category
from .models.donations import Donation
from .models.donors import Donor


# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    if has_role(request.user, ['consejo', 'admin']):
        context = {}
        return render(request, 'donations/index.html', context)
    else:
        raise Http404

# New DB entries

def new_donor(request):
    if has_role(request.user, ['consejo', 'admin']):
         context = { 'today': datetime.datetime.now() }
    
         if request.method == "POST":
    
             # Get the form through POST
             new_donor_form = DonorForm(request.POST)
    
             # Validate form data
             if new_donor_form.is_valid():
    
                 # Get form variables
                 # Create donor object
                 context['donor'] = Donor.objects.create(**new_donor_form.cleaned_data)
                 return list_donor(request)
    
             context['form'] = new_donor_form
             return render(request, 'donations/new_donor.html', context)
    
         else: new_donor_form = DonorForm()
    
         context['form'] = new_donor_form
         
         return render(request, 'donations/new_donor.html', context)
    else:
        raise Http404

def new_donation(request):
    if has_role(request.user, ['consejo', 'admin']):
        donors = Donor.objects.all().values('id', 'full_name')
        categories = Category.objects.all().values('id', 'name')
        context = {'categories': categories, 'donations': donors}
        
        if request.method == "POST":
            
            # Get the form through POST
            new_donation_form = DonationForm(request.POST)
            
            # Validate form data
            if new_donation_form.is_valid():
                # Get form variables
                # Create donation object
                context['donation'] = Donation.objects.create(**new_donation_form.cleaned_data)
                return list_donation(request)
            
            context['form'] = new_donation_form
            return render(request, 'donations/new_donation.html', context)
        
        else:
            new_donation_form = DonationForm()
        
        context['form'] = new_donation_form
        
        return render(request, 'donations/new_donation.html', context)
    
    else:
        raise Http404

def new_category(request):
    if has_role(request.user, ['consejo', 'admin']):
        context = {}
        
        if request.method == "POST":
            
            # Get the form through POST
            new_category_form = CategoriesForm(request.POST)
            
            # Validate form data
            if new_category_form.is_valid():
                # Get form variables
                # Create category object
                context['category'] = Category.objects.create(**new_category_form.cleaned_data)
                return list_category(request)
            
            context['form'] = new_category_form
            return render(request, 'donations/new_category.html', context)
        
        else:
            new_category_form = CategoriesForm()
        
        context['form'] = new_category_form
        
        return render(request, 'donations/new_category.html', context)
    else:
        raise Http404

#List CRUDs

def list_donor(request):
    if has_role(request.user, ['consejo', 'admin']):
        donors = Donor.objects.all().values()
    
        return render(request, 'donations/list_donors.html', {'donors': donors})
    else:
        raise Http404

def list_category(request):
    if has_role(request.user, ['consejo', 'admin']):
        categories = Category.objects.all().values()
        return render(request, 'donations/list_categories.html', {'categories': categories})
    else:
        raise Http404

def list_donation(request):
    if has_role(request.user, ['consejo', 'admin']):
        donations = Donation.objects.all()
        return render(request, 'donations/list_donations.html', {'donations': donations})
    else:
        raise Http404

#Delete from DB

def DonorDelete(request, pk):
    if has_role(request.user, ['consejo', 'admin']):
        model = get_object_or_404(Donor, pk=pk)
        model.delete()
        return HttpResponseRedirect(reverse('donations:list_donors'))
    else:
        raise Http404

def DonationDelete(request, pk):
    if has_role(request.user, ['consejo', 'admin']):
        model = get_object_or_404(Donation, pk=pk)
        model.delete()
        return HttpResponseRedirect(reverse('donations:list_donations'))
    else:
        raise Http404
 
def CategoryDelete(request, pk):
    if has_role(request.user, ['consejo', 'admin']):
        model = get_object_or_404(Category, pk=pk)
        model.delete()
        return HttpResponseRedirect(reverse('donations:list_categories'))
    else:
        raise Http404

#Update DB entries

class DonorUpdate(UpdateView):
        model = Donor
        fields = [
            'full_name',
            'integration_date',
            'state',
            'city',
            'street',
            'number',
            'reference',
            'contact_name',
            'contact_phone_number',
            'contact_email',
            'contact_birthday',
            'contact_anniversary'
        ]
        template_name = 'donations/donor_edit_form.html'
        slug_field = 'full_name'
        slug_url_kwarg = 'slug'
        success_url = '/donaciones/lista_donadores'
    
class DonationUpdate(UpdateView):
    model = Donation
    fields = ['donor', 'description', 'category']
    template_name = 'donations/donation_edit_form.html'
    slug_field = 'description'
    slug_url_kwarg = 'slug'
    success_url = '/donaciones/lista_donaciones'

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'donations/category_edit_form.html'
    slug_field = 'name'
    slug_url_kwarg = 'slug'
    success_url = '/donaciones/lista_categorias'


