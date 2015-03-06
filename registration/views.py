
from django.shortcuts import render, redirect

from django.http import HttpResponse
from registration.forms import UserCreationForm
# Create your views here.

def register(request, template_name='registration/registration_form.html'):
	args = {}
	
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = UserCreationForm()
	args['form'] = form
	return render(request, template_name, args)
