from django.http import HttpResponse
from django.shortcuts import render

from .models.families import Family
from .models.members import Member

from .forms.families import FamilyForm
from .forms.members import MemberForm


def index(request):
	all_families = Family.objects.all()
	member = Member.objects.get(familia = all_families)
	context = {
		'all_families': all_families,
		'member': member,
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
	context = { }
	newFamilyForm = FamilyForm()
	newDadForm = MemberForm()
	newMomForm = MemberForm()
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		newFamilyForm = FamilyForm(request.POST)
		newDadForm = MemberForm(request.POST)
		newMomForm = MemberForm(request.POST)
		
		familyValid = newFamilyForm.is_valid()
		dadValid = newDadForm.is_valid()
		MomValid = newMomForm.is_valid()
		
		# check whether it's valid:
		if familyValid and dadValid and MomValid:
			family = newFamilyForm.save()
			dad = newDadForm.save(commit=False)
			mom = newMomForm.save(commit=False)
			
			dad.familia = family
			dad.save()
			mom.familia = family
			mom.save()
			
			return read(request)
	context = {
		'newFamilyForm': newFamilyForm,
		'newDadForm': newDadForm,
		'newMomForm': newMomForm
	}
	return render(request, 'adoptions/family_form.html', context)
	
	# if a GET (or any other method) we'll create a blank form
	return render(request, 'adoptions/family_form.html', context)