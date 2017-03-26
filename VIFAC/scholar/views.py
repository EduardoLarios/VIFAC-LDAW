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