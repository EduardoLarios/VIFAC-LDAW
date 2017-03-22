from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    context = {}
    return render(request, 'dashboard/index.html', context)

