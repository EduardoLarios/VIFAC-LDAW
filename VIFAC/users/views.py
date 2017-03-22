from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, UpdateForm
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy


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
            
            #return User if credentials correct
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                if user.is_active:
                    login(request, user)
                    return redirect('/usuarios/lista_usuarios')
        return render(request, self.template_name, {'form': form})
    
    
def index(request):
    context = {}
    return render(request, 'users/index.html', context)


def login(request):
    context = {}
    return render(request, 'users/login.html', context)


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('users:lista_usuarios')


def list_users(request):
    queryset = User.objects.all().values()
    return render(request, 'users/list_users.html', {'users': queryset})


class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'users/editform.html'
    slug_field = 'username'
    slug_url_kwarg = 'slug'
    success_url = '/usuarios/lista_usuarios'
