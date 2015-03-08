from django.conf.urls import patterns, url
#from views import MedicalInfomationView
import views
from medicalinfo.views import MedicalinfoView

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>\d+)/$', MedicalinfoView.as_view(), name='patient-medicalinfo'),
	
)