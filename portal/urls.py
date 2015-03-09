from django.conf.urls import patterns, url
from portal import views
from portal.sitemap import *
from portal.views import (PortalHomeView, PortalContatoView, PortalPhotoLivroView, PortalPhotoLembrancaView,
							PortalPhotoGramView, PortalPhotoProjecaoView, PortalPhotoEmpresaView, enviar_contato,
							PortalBlogView,)

sitemaps = {
    'pages':PortalSitemap(['Portal', 'PhotoLivro', 'PhotoLembranca', 'PhotoGram', 'PhotoProjecao',
     'PhotoEmpresa', 'Contato']),
}

urlpatterns = patterns('',
	url(r'^/?$',  PortalHomeView.as_view(), name="Portal"),
	url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
	url(r'^photolivro/?$',  PortalPhotoLivroView.as_view(), name="PhotoLivro"),
	url(r'^photolembranca/?$',  PortalPhotoLembrancaView.as_view(), name="PhotoLembranca"),
	url(r'^photogram/?$',  PortalPhotoGramView.as_view(), name="PhotoGram"),
	url(r'^photoprojecao/?$',  PortalPhotoProjecaoView.as_view(), name="PhotoProjecao"),
	url(r'^photoempresa/?$',  PortalPhotoEmpresaView.as_view(), name="PhotoEmpresa"),
	url(r'^contato/?$',  PortalContatoView.as_view(), name="Contato"),
	url(r'^enviar_contato/?$',  enviar_contato, name="EnviarContato"),
	url(r'^blog/?$',  PortalBlogView.as_view(), name="Blog"),
	)
