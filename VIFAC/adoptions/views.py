from django.http import HttpResponse
from django.shortcuts import render
import datetime


from .models.families import Family

from .forms.families import FamilyForm


def index(request):
	all_families = Family.objects.all()
	context = {
		'all_families': all_families
	}
	return render(request, 'adoptions/index.html', context)


def detail(request, family_id):
	return HttpResponse("<h1> Detalles " + str(family_id) + "</h1>")


def read(request):
	all_families = Family.objects.all()
	context = {
		'all_families': all_families
	}
	return render(request, 'adoptions/ver_familias.html', context)


def add_Family(request):
	context = {'today': datetime.datetime.now()}
	
	if request.method == "POST":
		
		newFamilyForm = FamilyForm(request.POST, prefix="fam")
		
		if newFamilyForm.is_valid():
			context['family'] = Family.objects.create(**newFamilyForm.cleaned_data)
			return read(request)
		
		context['form'] = newFamilyForm
		return render(request, 'adoptions/family_form.html', context)

	return render(request, 'adoptions/family_form.html', context)
