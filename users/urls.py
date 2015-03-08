from django.conf.urls import patterns, url

from users import views
from views import UserProfileView, UserProfileUpdate

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	#url(r'^(?P<user_id>\d+)/$',views.view_profile, name='view_profile'),
	url(r'^(?P<pk>\d+)/$', UserProfileView.as_view(), name='userprofile-detail'),
	#url(r'^profile/$', views.edit_profile , name='userprofile-edit')
	url(r'^(?P<pk>\d+)/update', UserProfileUpdate.as_view(), name='userprofile-update'),
	
)