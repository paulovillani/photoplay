from django.conf.urls import patterns, url, include
from blog.views import PortalBlogView


urlpatterns = patterns('',
	url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
	url(r'^comments/', include('django_comments.urls')),
	url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
	url(r'^blog/?$', PortalBlogView.as_view(), name="Blog"),
	)
