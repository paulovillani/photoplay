from django.conf.urls import patterns, url, include
from blog.views import BlogListView, PostView


urlpatterns = patterns('',
	url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
	url(r'^comments/', include('django_comments.urls')),
	(r'^tinymce/', include('tinymce.urls')),
	url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
	url(r'^blog/?$', BlogListView.as_view(), name="Blog"),
	url(r'^blog/categoria/(?P<category>[-_\w]+)/?$', BlogListView.as_view(), name='Category'),
	url(r'^blog/(?P<slug>[-_\w]+)/$', PostView.as_view(), name='Post'),
	)
