from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password =  forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields  = ['username', 'email','first_name','last_name', 'password']


class UpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']

#class UserRole(forms.Form):
