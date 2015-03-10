from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, FormView

# Create your views here.

class PortalBlogView(TemplateView):
	template_name = "blog.html"	