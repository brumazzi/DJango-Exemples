from __future__ import unicode_literals

from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField()
    tell = models.CharField(max_length=13)

    def __str__(self):
        return self.nome

class Message(models.Model):
    texto = models.CharField(max_length=400)
    contato = models.ForeignKey(Contato)
