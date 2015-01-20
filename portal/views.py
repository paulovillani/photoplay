# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, FormView

# Create your views here.

class PortalHomeView(TemplateView):
    template_name = "portal_home.html"

class PortalProdutosView(TemplateView):
	template_name = "produtos.html"