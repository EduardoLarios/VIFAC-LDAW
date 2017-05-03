from django.shortcuts import render, get_object_or_404
from .forms import AsignPanfletForm, ParticipanteForm
from .models import Panfleta, Participante
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from rolepermissions.checkers import has_role
from django.http import Http404

# Create your views here.
app_name = 'raffles'

def index(request):
    if has_role(request.user, ['consejo', 'admin']):
        if request.method == "GET":
            if 'busqueda_part' in request.GET:
                name = request.GET["busqueda_part"]
                query = Participante.objects.filter(full_name__icontains=name)
                if query:
                    context = {
                        'participantes': query
                    }
                else:
                    res = True
                    context = {
                        'no_results': res
                    }
                return render(request, 'raffles/index.html', context)
            if 'busqueda_panf' in request.GET:
                folio = request.GET["busqueda_panf"]
                query = Panfleta.objects.filter(folio__icontains=folio)
                if query:
                    context = {
                        'panfletas': query
                    }
                else:
                    res = True
                    context = {
                        'no_results': res
                    }
                return render(request, 'raffles/index.html', context)
        return render(request, 'raffles/index.html')
    else:
        raise Http404

def assign_form(request, participant_id):
    if has_role(request.user, ['consejo', 'admin']):
        form = AsignPanfletForm(request.POST or None)
        part = get_object_or_404(Participante, pk=participant_id)
        if form.is_valid():
            folios_part = part.panfleta_set.all()
            for pan in folios_part:
                if pan.folio == form.cleaned_data.get("folio"):
                    context = {
                        'participante': part,
                        'form': form,
                        'error_message': 'Ese folio ya existía',
                    }
                    return render(request, 'raffles/new_raffle.html', context)
            panfleta = form.save(commit=False)
            panfleta.participante = part
            panfleta.save()
    
            if '_addother' in request.POST:
                form = AsignPanfletForm()
                context = {
                    'participante': part,
                    'panfleta': panfleta,
                    'form': form,
                }
                return render(request, 'raffles/new_raffle.html', context)
            else:
                return HttpResponseRedirect(reverse('raffles:panfletas_part', args=(part.id,)))
            # return render(request, 'raffles/index.html', {'album': album})
    
        context = {
            'participante': part,
            'form': form,
        }
        return render(request, 'raffles/new_raffle.html', context)
    raise Http404

def panfletas_part(request, participant_id):
    if has_role(request.user, ['consejo', 'admin']):
        part = get_object_or_404(Participante, pk=participant_id)
        panfletas = part.panfleta_set.all()
        context = {
            'participante': part,
            'panfletas': panfletas,
        }
        return render(request, 'raffles/panfleta_part.html', context)
    else:
        raise Http404

def nuevo_participante(request):
    if has_role(request.user, ['consejo', 'admin']):
        if request.method == "POST":
            name = request.POST['name']
            phone = request.POST['phone']
            part = Participante(full_name=name, phone_number=phone)
            part.save()
            return HttpResponseRedirect(reverse('raffles:assign_panflet', args=(part.id,)))
    else:
        raise Http404


    return render(request, 'raffles/new_participant.html')

class PanfletaEdit(UpdateView):
    model = Panfleta
    template_name = 'raffles/panfleta_detail.html'
    success_url = reverse_lazy('raffles:index')
    fields = ['devuelta', 'monto_entregado']


def delete_panfleta(request):
    if has_role(request.user, ['consejo', 'admin']):
        if request.method == "POST":
            Panfleta.objects.filter(pk__in=request.POST.getlist('item')).delete()
            part = Participante.objects.get(pk=request.POST["id_part"])
        return HttpResponseRedirect(reverse('raffles:panfletas_part', args=(part.id,)))
    else:
        raise Http404

class ParticipanteEdit(UpdateView):
    model = Participante
    template_name = 'raffles/participante_detail.html'
    success_url = reverse_lazy('raffles:index')


def delete_participante(request, participant_id):
    if has_role(request.user, ['consejo', 'admin']):
        part = Participante.objects.get(pk=participant_id)
        part.delete()
        return reverse_lazy('raffles:index')
    else:
        raise Http404
