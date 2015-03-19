# -*- coding: utf-8 -*-
from django import forms

class NewsletterForm(forms.Form):
	name = forms.CharField(
		label='',
		widget=forms.TextInput(
            attrs={"placeholder": u"Nome:"}), 
		required=True,
	)
	email = forms.EmailField(
		label='',
		widget=forms.TextInput(
            attrs={"placeholder": u"Email:"}), 
		required=True
	)