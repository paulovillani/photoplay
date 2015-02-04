# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, FormView
from forms import ContactForm

# Create your views here.

class PortalHomeView(TemplateView):
    template_name = "portal_home.html"

class PortalPhotoLivroView(TemplateView):
	template_name = "produtos_photolivro.html"

class PortalPhotoLembrancaView(TemplateView):
	template_name = "produtos_photolembraca.html"

class PortalPhotoGramView(TemplateView):
	template_name = "produtos_photogram.html"

class PortalPhotoProjecaoView(TemplateView):
	template_name = "produtos_photoprojecao.html"

class PortalPhotoEmpresaView(TemplateView):
	template_name = "produtos_photoempresa.html"

class PortalContatoView(TemplateView):
	template_name = "contato.html"

	def get_context_data(self, **kwargs):
		context = super(PortalContatoView, self).get_context_data(**kwargs)
		context['contact_form'] = ContactForm()

		return context