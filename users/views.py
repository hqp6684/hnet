from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
@login_required(login_url='/login')
def index(request):
	if not request.user.is_staff:
		return HttpResponseRedirect("/")
	
	users = User.objects.all()
	context = {'users_list' : users}
	
	return render(request, 'users/index.html', context)

	
