from django.shortcuts import render
from .models.families import Family
from django.http import HttpResponse

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
	context={}
	return render(request, 'adoptions/family_form.html', context)
