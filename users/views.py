from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	users = User.objects.all()
	context = {'users_list' : users}
	
	return render(request, 'users/index.html', context)