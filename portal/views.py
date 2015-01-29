# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, FormView
from forms import ContactForm

# Create your views here.

class PortalHomeView(TemplateView):
    template_name = "portal_home.html"

class PortalProdutosView(TemplateView):
	template_name = "produtos.html"

class PortalContatoView(TemplateView):
	template_name = "contato.html"

	def get_context_data(self, **kwargs):
		context = super(PortalContatoView, self).get_context_data(**kwargs)
		context['contact_form'] = ContactForm()

		return context