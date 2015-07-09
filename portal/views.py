# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, FormView
from forms import ContactForm
from django.core.mail import send_mail
from municipios.models import Municipio, UF
from django.db.models import Q
from portal.models import Contact, Budget, PodioConfig
from pypodio2 import api
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

# Create your views here.

class PortalHomeView(TemplateView):
    template_name = "bootstrap_home.html"

class PortalPhotoLivroView(TemplateView):
	template_name = "photolivro.html"

class PortalPhotoLembrancaView(TemplateView):
	template_name = "photolembranca.html"

class PortalPhotoGramView(TemplateView):
	template_name = "photogram.html"

class PortalPhotoProjecaoView(TemplateView):
	template_name = "photoprojecao.html"

class PortalPhotoEmpresaView(TemplateView):
	template_name = "photoempresa.html"

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
			tel = 			form.cleaned_data['tel']
			email = 		form.cleaned_data['email']
			date_start = 	form.cleaned_data['date_start']
			message = 		form.cleaned_data['message']

			a = Municipio.objects.get(id_ibge = municipios)

			cidade = a.nome
			uf = a.uf.nome

			msg = u"O usuário '"+name+"', email: "+email+", telefone: "+tel+", envi'ou um contato pelo site.\n"
			msg+= u"Tipo de evento: "
			if service_type == 1:
				msg+="Casamento"
			elif service_type == 2:
				msg+="Aniversário"
			elif service_type == 3:
				msg+="Formatura"
			elif service_type == 4:
				msg+="Corporativo"
			else:
				msg+="Outro"
			msg+="\n"
			msg+= u"Cidade: "+cidade+", Estado: "+uf+"\n"
			msg+= "Dia do evento: "+str(date_start)+"\n"
			msg+= u"Mensagem: "+message

			try:
				contato = Contact.objects.get(Q(email=email))
			except Contact.DoesNotExist:
				contato = Contact(
					name = name,
					email = email,
					tel = tel,
					city = cidade,
					state = a.uf.uf,
				)
				contato.save()

			orcamento = Budget(
				event_type = service_type,
				contact = contato,
				date = date_start,
				message = message,
			)
			orcamento.save()
			# podio = PodioConfig.objects.get(pk=1)

			# c = api.OAuthClient(
			#     podio.client_id,
			#     podio.client_secret,
			#     podio.username,
			#     podio.password,    
			# )

			# item = {
			# 	"fields":[{
			# 		"company-or-organisation": name,
			# 		"email": email,
			# 		"sales-contact": 2758134,
			# 		"tipo-de-evento": 1,
			# 		"status2": 0,
			# 		"next-follow-up": {"start":"2015-03-11 00:00:00","end":"2112-01-31 00:00:00"},
			# 		"street-address": "",
			# 		"city": cidade,
			# 		"state-provins-or-territory": a.uf.uf,
			# 		"address": ""
			# 	}]
			# }
			# print item

			# c.Item.create(int(podio.app_id), item)

			send_mail("Orçamento PhotoPlay", msg, 'noreply@photoplay.com.br', 
				['equipe@photoplay.com.br', 'contato@photosite.webfactional.com'] )


			return render(request, 'contato_sucesso.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'contato.html', {'contact_form': form})

@csrf_exempt
def receber_lead(request):
    	# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = json.loads(request.body)

		nome = form['nome']
		tel = form['tel']
		email = form['email']
		tipo = form['tipo']
		data = form['data']
		estado = form['estado']
		cidade = form['cidade']
		como_conheceu = form['como_conheceu']
		codigo = form['codigo']

		msg = u"Lead recebido pelo site do Fottorama:\n"
		msg+= u"Nome: '"+nome+"'\n"
		msg+= u"Telefone: '"+tel+"'\n"
		msg+= u"Email: '"+email+"'\n"
		msg+= u"Tipo de evento: '"+tipo+"'\n"
		if tipo == 1:
			msg+="Casamento\n"
		elif tipo == 2:
			msg+="Corporativo\n"
		elif tipo == 3:
			msg+="Aniversário\n"
		elif tipo == 4:
			msg+="Formatura\n"
		elif tipo == 5:
			msg+="Universitário\n"
		else:
			msg+="Outro\n"
		
		msg+= u"Data: '"+data+"'\n"
		msg+= u"Estado: '"+estado+"'\n"
		msg+= u"Cidade: '"+cidade+"'\n"
		msg+= u"Como conheceu: "
		if como_conheceu == 1:
			msg+="'Vi propaganda no Facebook'\n"
		elif como_conheceu == 2:
			msg+="'Busquei no Google'\n"
		elif como_conheceu == 3:
			msg+="'Em uma Feira de Noivas'\n"
		elif como_conheceu == 7:
			msg+="'Revista'\n"
		elif como_conheceu == 4:
			msg+="'Vi em um evento e gostei'\n"
		elif como_conheceu == 5:
			msg+="'Um amigo me recomendou'\n"
		else:
			msg+="'Por outro meio'\n"
		msg+= u"Código Promocional: '"+codigo+"'\n"

		send_mail("Orçamento PhotoPlay", unicode(msg), 'noreply@photoplay.com.br', 
		['equipe@photoplay.com.br', 'contato@photosite.webfactional.com'] )

		return HttpResponse("200 ok")