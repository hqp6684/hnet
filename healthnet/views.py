from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def home(request, template='index.html'):
	return render(request, template)