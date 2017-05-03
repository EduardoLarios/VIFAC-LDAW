from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import UpdateView

from django.template import loader, Context

from .models.families import Family
from .models.members import Member

from .forms.families import FamilyForm
from .forms.members import MemberForm


def index(request):
	all_families = Family.objects.all()
	context = {
		'all_families': all_families,
	}
	return render(request, 'adoptions/index.html', context)


def read(request):
	all_families = Family.objects.all()
	dad = Member
	mom = Member
	for family in all_families:
		dad = Member.objects.get(familia=family, Genero='Masculino')
		mom = Member.objects.get(familia=family, Genero='Femenino')
	context = {
		'all_families': all_families,
		'dad': dad,
		'mom': mom
	}
	return render(request, 'adoptions/ver_familias.html', context)


def buscar(request):
	all_families = Family.objects.all()
	for family in all_families:
		dad = Member.objects.get(familia=family, Genero='Masculino')
		mom = Member.objects.get(familia=family, Genero='Femenino')
		
	context = {
		'all_families': all_families,
		'dad': dad,
		'mom': mom
	}
	
	query = request.GET['q']
	try:
		family = Family.objects.filter(nombreFam = query)
		context ={
			'family': family
		}
		return render(request, 'adoptions/family_busqueda.html', context)
	except:
		return render(request, 'adoptions/ver_familias.html', context)


def add_Family(request):
	context = {}
	newFamilyForm = FamilyForm(prefix='Fam')
	newDadForm = MemberForm(prefix='Dad')
	newMomForm = MemberForm(prefix='Mom')
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		newFamilyForm = FamilyForm(request.POST, prefix='Fam')
		newDadForm = MemberForm(request.POST, prefix='Dad')
		newMomForm = MemberForm(request.POST, prefix='Mom')
		familyValid = newFamilyForm.is_valid()
		dadValid = newDadForm.is_valid()
		MomValid = newMomForm.is_valid()
		# check whether it's valid:
		if familyValid and dadValid and MomValid:
			family = newFamilyForm.save()
			dad = newDadForm.save(commit=False)
			mom = newMomForm.save(commit=False)
			dad.familia = family
			dad.Genero = 'Masculino'
			dad.save()
			mom.familia = family
			mom.Genero = 'Femenino'
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


class FamilyUpdate(UpdateView):
	model = Family
	fields = ['nombreFam',
	          'Aniversario',
	          'actaMatrimonioCivil',
	          'actaMatrimonioReligioso',
	          'estudioSC',
	          'comprobanteDom',
	          'comprobanteResidencia',
	          'cartasRecomendacion',
	          'cartasRecomendacionSacerdotal',
	          'cartaAbuelosPaternos',
	          'cartaAbuelosMaternos',
	          'estudioPsi',
	          'certificadoIdoneidad',
	          'fotosFamiliares',
	          'cartaDIF',
	          'cursoPadres',
	          'status',
	          'motivoBaja',
	          'fBaja',
	          'nombreMamaBio',
	          'fAdopcion',
	          ]
	template_name = 'adoptions/family_edit_form.html'
	slug_field = 'name'
	slug_url_kwarg = 'slug'
	success_url = reverse_lazy('read')


class MemberUpdate(UpdateView):
	model = Member
	fields = ['nombre',
	          'aPaterno',
	          'aMaterno',
	          'FNacimiento',
	          'Estado',
	          'Telefono',
	          'autobiografia',
	          'actaNacimiento',
	          'fotos',
	          'certificadoMedico',
	          'analisisVIH',
	          'antecedentesPenales',
	          'identificacion',
	          ]
	template_name = 'adoptions/member_edit_form.html'
	slug_field = 'nombre'
	slug_url_kwarg = 'slug'
	success_url = reverse_lazy('read')


def FamilyDelete(request, pk):
	model = get_object_or_404(Family, pk=pk)
	model.delete()
	return HttpResponseRedirect(reverse('read'))