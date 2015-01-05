from django.conf.urls import patterns, url
from portal import views
from portal.views import (PortalHomeView)

urlpatterns = patterns('',
	url(r'^/?$',  PortalHomeView.as_view(), name="Portal"),
)