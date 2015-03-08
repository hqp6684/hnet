from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from models import UserProfile
from forms import UserProfileForm

from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse

# Create your views here.
@login_required(login_url='/login')
def index(request):
	if not request.user.is_staff:
		return HttpResponseRedirect("/")

	users = User.objects.all()
	context = {'users_list' : users}
	
	return render(request, 'users/index.html', context)

	
class UserProfileView(DetailView):
	model = UserProfile
	template_name = "users/user_profile.html"



class UserProfileUpdate(UpdateView):
	#template_name = 'users/user_edit_form.html'
	#form_class = UserProfileForm
	model = UserProfile
	form_class = UserProfileForm
	#fields = ['sSN', 'dOB','email']
	template_name_suffix = '_update_form'
	#return render_to_response(self.template_name, self.get_context_data())
