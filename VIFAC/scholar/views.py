from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import AsignarMaterial, EscuelaForm
from .models import Escuela, Material
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

app_name = 'scholar'

def index(request):
    return render(request, 'scholar/index.html')


def nueva_escuela(request):
    if request.method == "POST":
        name = request.POST['name']
        ciudad = request.POST['ciudad']
        estado = request.POST['estado']
        part = Escuela(name = name, ciudad=ciudad, estado=estado)
        part.save()
        return HttpResponseRedirect(reverse('scholar:index'))

    return render(request, 'scholar/new_school.html')


def list_escuelas(request):
    queryset = Escuela.objects.all().values()
    return render(request, 'scholar/escuela_list.html', {'escuelas:': queryset})


class EscuelasListView(ListView):
    model = Escuela


class EscuelaUpdate(UpdateView):
    model = Escuela
    fields = ['name', 'estado', 'ciudad']
    template_name = 'scholar/escuelaedit.html'
    slug_field = 'description'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('scholar:list_escuela')


def delete_escuela(request, pk):
    escuela = get_object_or_404(Escuela, pk=pk)
    escuela.delete()
    return HttpResponseRedirect(reverse('scholar:list_escuela'))


def asignar_material(request, escuela_id):
    form = AsignarMaterial(request.POST or None)
    escuela = get_object_or_404(Escuela, pk=escuela_id)
    if form.is_valid():
        material = form.save(commit=False)
        material.escuela = escuela
        material.save()

        if '_addother' in request.POST:
            form = AsignarMaterial()
            context = {
                'Escuela': escuela,
                'form': form,
            }
            return render(request, 'scholar/new_material.html', context)
        else:
            return HttpResponseRedirect(reverse('scholar:list_escuela'))
            #return HttpResponseRedirect(reverse('raffles:panfletas_part', args=(part.id,)))

    context = {
        'escuela': escuela,
        'form': form,
    }
    return render(request, 'scholar/new_material.html', context)


def material_escuela(request, escuela_id):
    escuela = get_object_or_404(Escuela, pk=escuela_id)
    materiales = escuela.material_set.all()
    context = {
        'escuela': escuela,
        'materiales': materiales,
    }
    return render(request, 'scholar/materiales_escuela.html', context)