from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import UpdateView
from django.urls import reverse_lazy, reverse

def index(request):
    return render(request, 'medical/index.html')