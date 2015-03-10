from django.conf.urls import patterns, url
from blog.views import PortalBlogView


urlpatterns = patterns('',
	url(r'^blog/?$',  PortalBlogView.as_view(), name="Blog"),
	)
