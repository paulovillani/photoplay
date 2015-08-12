from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url('', include('social.apps.django_app.urls', namespace='social')),
	url('', include('django.contrib.auth.urls', namespace='auth')),
	url(r'^publicador/$', 'publicador.views.home', name='home'),
	#url(r'^publicador/admin/', include(admin.site.urls)),
)