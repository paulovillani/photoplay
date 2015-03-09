# -*- coding: utf-8 -*-
from django import forms
from municipios.widgets import SelectMunicipioWidget
from portal.models import EVENT_CHOICES

class ContactForm(forms.Form):
	service_type = forms.ChoiceField(
		# widget=forms.TextInput(
		#     attrs={"placeholder": u"Cidade"}),
		widget=forms.RadioSelect,
		choices = EVENT_CHOICES,
		required=True, 
		label="QUAL TIPO DE EVENTO?"
	)
	municipios = forms.IntegerField(
		label=u"QUAL A LOCALIZAÇÃO DO EVENTO?",
		widget=SelectMunicipioWidget,
		required=True
	)
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