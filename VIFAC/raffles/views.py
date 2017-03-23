from django.shortcuts import render, get_object_or_404
from .forms import AsignPanfletForm, PanfletForm, Participante
from .models import Panfleta, Participante
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'raffles/index.html')

def assign_form(request, participant_id):
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
            return reverse_lazy('raffles:index')
        # return render(request, 'raffles/index.html', {'album': album})

    context = {
        'participante': part,
        'form': form,
    }
    return render(request, 'raffles/new_raffle.html', context)


def new_participant(request, participant_id):
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
            return reverse_lazy('raffles:index')
        # return render(request, 'raffles/index.html', {'album': album})

    context = {
        'participante': part,
        'form': form,
    }
    return render(request, 'raffles/new_raffle.html', context)

class PanfletaEdit(UpdateView):
    model = Panfleta
    template_name = 'raffles/panfleta_detail.html'
    success_url = reverse_lazy('raffles:index')
    fields = ['devuelta', 'monto_entregado']
