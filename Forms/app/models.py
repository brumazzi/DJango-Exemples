#*-* coding:utf-8 *-*
from __future__ import unicode_literals

from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome',max_length=60)
    nasci = models.DateField()
    descr = models.TextField('Descrição')

