# -*- coding: utf-8 -*-
from django.db import models

EVENT_CHOICES = [
    ['1', 'Casamento'],
    ['2', u'Aniversário'],
    ['3', 'Formatura'],
    ['4', 'Corporativo'],
    ['5', 'Outro']
]

class Contact(models.Model):
    class Meta:
        verbose_name = u"Contato"
        verbose_name_plural = u"Contatos"

    name = models.CharField(max_length=256, verbose_name=u"Nome")
    email = models.EmailField(max_length=128)
    city = models.CharField(max_length=128, verbose_name=u"Cidade")
    state = models.CharField(max_length=2, verbose_name=u"Estado")

    def __unicode__(self):
        return self.name

class Budget(models.Model):
    class Meta:
        verbose_name = u"Orçamento"
        verbose_name_plural = u"Orçamentos"

    event_type = models.CharField(max_length=1, choices=EVENT_CHOICES, verbose_name=u"Tipo de evento")
    contact = models.ForeignKey(Contact, verbose_name=u"Contato")
    date = models.DateField(verbose_name=u"Data do evento")
    message = models.TextField(verbose_name=u"Mensagem")

    def __unicode__(self):
        return self.contact.name

class PodioConfig(models.Model):
	client_id = models.CharField(max_length=256)
	client_secret = models.CharField(max_length=512)
	username = models.CharField(max_length=256)
	password = models.CharField(max_length=256)
	app_id = models.CharField(max_length=256)