from rolepermissions.roles import assign_role, remove_role, get_user_roles, clear_roles
from django.views.generic.edit import DeleteView, UpdateView
from django.http import Http404, HttpResponseRedirect, HttpResponse
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from rolepermissions.checkers import has_role
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, UpdateForm
from django.views.generic import View
from django.urls import reverse
from VIFAC.roles import *
import csv


class UserFormView(View):
    form_class = UserForm
    template_name = 'users/registrationform.html'
    
    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('/usuarios/lista_usuarios/')

        return render(request, self.template_name, {'form': form})
            
    
def index(request):
    context = {}
    if request.user.is_authenticated():
        if has_role(request.user, ['consejo', 'admin']):
            return render(request, 'users/index.html', context)
        else:
            raise Http404
    else:
        return redirect('/usuarios/login/')


def UserDelete(request, pk):
    if has_role(request.user, ['consejo', 'admin']):
        usuario = get_object_or_404(User, pk=pk)
        usuario.delete()
        return HttpResponseRedirect(reverse('users:lista_usuarios'))
    else:
        raise Http404


def list_users(request):
    if has_role(request.user, ['consejo', 'admin']):
        queryset = User.objects.all()
        role = []
        count = 0
        for user in queryset:
            role.append(get_user_roles(user))
            count += 1
            print(role)
    
        context = {
            'users': queryset,
            'roles': role,
        }
        return render(request, 'users/list_users.html', context)
    else:
        raise Http404


class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'users/editform.html'
    slug_field = 'username'
    slug_url_kwarg = 'slug'
    success_url = '/usuarios/lista_usuarios'


def login(request):
    context = {}
    return render(request, 'users/login.html', context)


def asignar_rol(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "POST":
        rol = request.POST["rol"]
        clear_roles(user)
        assign_role(user, rol)
        return HttpResponseRedirect(reverse('users:asignar_rol', args=(user_id)))
    else:

        context = {
            'user': user,
        }
        return render(request, 'users/assign_role.html', context)


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Usuario', 'Nombre', 'Apellidos', 'Email'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response
