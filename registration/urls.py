from django.conf.urls import patterns, url
from registration import views

urlpatterns = patterns('',
	url(r'^$', views.register, name='register'),
	url(r'^employee/$', views.register_employee, name='register-employee')

	
)