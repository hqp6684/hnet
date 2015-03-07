from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#include((pattern_list, app_namespace, instance_namespace))
urlpatterns = patterns('',    
	url(r'^$', 'login.views.loginTest1', name='loginUser'),
	url(r'^loggedin', 'login.views.login_redirect', name='login_redirect'),
	url(r'^logout/', 'login.views.logout', name='logout'),


)