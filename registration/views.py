from django.shortcuts import render, redirect

from django.http import HttpResponse
from registration.forms import UserCreationForm
# Create your views here.

def register(request, template_name='registration/registration_form.html'):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request, template_name, {'form':form})