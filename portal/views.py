# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, FormView
from forms import ContactForm
from django.core.mail import send_mail
from municipios.models import Municipio, UF

# Create your views here.

class PortalHomeView(TemplateView):
    template_name = "portal_home.html"

class PortalPhotoLivroView(TemplateView):
	template_name = "produtos_photolivro.html"

class PortalPhotoLembrancaView(TemplateView):
	template_name = "produtos_photolembranca.html"

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

def enviar_contato(request):
		# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
			service_type = 	form.cleaned_data['service_type']
			municipios = 	form.cleaned_data['municipios']
			name = 			form.cleaned_data['name']
			email = 		form.cleaned_data['email']
			date_start = 	form.cleaned_data['date_start']
			message = 		form.cleaned_data['message']

			a = Municipio.objects.get(id_ibge = municipios)

			cidade = a.nome
			uf = a.uf.nome

			msg = u"O usuário '"+name+"', email: "+email+", enviou um contato pelo site.\n"
			msg+= u"Tipo de serviço: "+service_type+"\n"
			msg+= u"Cidade: "+cidade+", Estado: "+uf+"\n"
			msg+= "Dia do evento: "+str(date_start)+"\n"
			msg+= u"Mensagem: "+message


			send_mail("Contato pelo site", msg, 'noreply@photoplay.com.br', 
				['equipe@photoplay.com.br', 'contato@photosite.webfactional.com'] )


			return render(request, 'contato_sucesso.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'contato.html', {'contact_form': form})