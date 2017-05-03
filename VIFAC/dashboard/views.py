from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    context = {}
    if request.user.is_authenticated():
        return render(request, 'dashboard/index.html', context)
    else:
        return redirect('/usuarios/login/')

