
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
from models import Medicalinfo
# Create your views here.
def index(request):
	medicalinfo = Medicalinfo.objects.all()
	template_name='medicalinfo/medicalinfo_index.html'
	context = {'medicalinfo': medicalinfo}
	return render(request,template_name,context)	

class MedicalinfoView(DetailView):
	model = Medicalinfo
	template_name = "medicalinfo/medicalinfo_view.html"
	