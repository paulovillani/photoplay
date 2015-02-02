# -*- coding: utf-8 -*-
from django import forms

SERVICE_CHOIVCES = (('casamento', 'Casamento'),
					('aniversario', u'Aniversário'),
					('formatura', 'Formatura'),
					('corporativos', 'Corporativo'),
					('outro', 'Outro'))

class ContactForm(forms.Form):
	service_type = forms.ChoiceField(
		# widget=forms.TextInput(
		#     attrs={"placeholder": u"Cidade"}),
		widget=forms.RadioSelect,
		choices = SERVICE_CHOIVCES,
		required=True, 
		label="QUAL TIPO DE EVENTO?"
	)
	#service_type = forms.ChoiceField(
		# widget=forms.TextInput(
		#     attrs={"placeholder": u"Cidade"}),
	#	choices = [u'Casamento', "Aniversário", "Formatura", "Corporativo", "Outro"],
#		required=True, 
#		label="QUAL A CIDADE MAIS PRÓXIMA DO EVENTO?"
#	)
	name = forms.CharField(
		label="PREENCHA OS CAMPOS ABAIXO",
		widget=forms.TextInput(
            attrs={"placeholder": u"Seu nome (obrigatório)"}), 
		required=True,
	)
	email = forms.EmailField(
		label="",
		widget=forms.TextInput(
            attrs={"placeholder": u"Seu e-mail (obrigatório)"}), 
		required=True
	)
	date_start = forms.DateField(
		label="",
		widget=forms.TextInput(
		attrs={"class": "datepicker", "placeholder": u"Data do evento"}),
		required=True
	)
	message = forms.CharField(
		widget=forms.Textarea(
            attrs={"placeholder": u"Sua mensagem"}),
		label="",
		required=True
	)