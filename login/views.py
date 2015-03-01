from django.shortcuts import render, render_to_response, redirect


# Create your views here.
from django.contrib.auth import authenticate, login
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from login.forms import loginForm, AuthenticationForm
from healthnet.views import home


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout
from django.core.context_processors import csrf

from django.core.urlresolvers import reverse_lazy

'''
def login(request, template_name='login/login.html'):
	form = AuthenticationForm(request.POST or None)
	if request.POST and form.is_valid():
		user = form.get_user
		return redirect('index')
	
	return render(request, template_name, {'form':form})
'''

def index_test(request):
	return HttpResponse("hello world")


	return render(request, template_name,{'form':form})
# Login user method
def loginUser(request):
    # Checks if user is already logged in
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")  # Redirect to home
    form = loginForm(request.POST or None)
    # Logs in user and sends user to a page redirect
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/")  # Redirect to a success page.
    return render(request, 'login/login.html', {'form': form})

def loginTest1(request):
	if request.method =='POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			login(request,form.get_user())
			return HttpResponseRedirect('/')
		else:
			HttpResponse("invalid")
	else:
		form = AuthenticationForm
	return render(request, 'login/login.html',{'form':form})

