from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login

from login.forms import loginForm

from django.http import HttpResponseRedirect, HttpResponse


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

