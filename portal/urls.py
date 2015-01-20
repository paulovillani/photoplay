from django.conf.urls import patterns, url
from portal import views
from portal.views import (PortalHomeView, PortalProdutosView)

urlpatterns = patterns('',
	url(r'^/?$',  PortalHomeView.as_view(), name="Portal"),
	url(r'^produtos/?$',  PortalProdutosView.as_view(), name="Produtos"),
)