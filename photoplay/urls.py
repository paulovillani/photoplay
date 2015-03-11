from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from filebrowser.sites import site
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^municipios_app/', include('municipios.urls')),
    url(r'^', include('portal.urls')),
    url(r'^', include('blog.urls')),
)
