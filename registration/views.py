
from django.shortcuts import render, redirect

from django.http import HttpResponse
from registration.forms import UserCreationForm, EmployeeCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request, template_name='registration/registration_form.html'):
	args = {}
	
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login')
	else:
		form = UserCreationForm()
	args['form'] = form
	return render(request, template_name, args)

@login_required(login_url='/login')
def register_employee(request, 
	template_name='registration/registration_employee_form.html'):
	args = {}
	

	if request.method =='POST':
		form = EmployeeCreationForm(request.POST)
		if form.is_valid():
			form.saveEmployee()
			return redirect('/login')
	else:
		form = EmployeeCreationForm()
	args['form'] = form
	return render(request, template_name, args)
