from django.conf.urls import patterns, url
from portal import views
from portal.views import (PortalHomeView, PortalContatoView, PortalPhotoLivroView, PortalPhotoLembrancaView,
							PortalPhotoGramView, PortalPhotoProjecaoView, PortalPhotoEmpresaView)

urlpatterns = patterns('',
	url(r'^/?$',  PortalHomeView.as_view(), name="Portal"),
	url(r'^photolivro/?$',  PortalPhotoLivroView.as_view(), name="PhotoLivro"),
	url(r'^photolembraca/?$',  PortalPhotoLembrancaView.as_view(), name="PhotoLembranca"),
	url(r'^photogram/?$',  PortalPhotoGramView.as_view(), name="PhotoGram"),
	url(r'^photoprojecao/?$',  PortalPhotoProjecaoView.as_view(), name="PhotoProjecao"),
	url(r'^photoempresa/?$',  PortalPhotoEmpresaView.as_view(), name="PhotoEmpresa"),
	url(r'^contato/?$',  PortalContatoView.as_view(), name="Contato"),
)