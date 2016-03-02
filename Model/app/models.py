#!/usr/bin/env python
#*-* coding:utf-8 *-*
from __future__ import unicode_literals

from django.db import models

class Agencia(models.Model):
    nome = models.CharField(max_length=60)
    site = models.URLField()

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField('Titulo', max_length=80)
    url = models.SlugField(
                'URL',
                max_length=200,
                help_text='URL baseada no título',
                unique=True)
    pub_date = models.DateTimeField('Data de publicação:')
    conteudo = models.TextField('Conteúdo da página:')
    autores = models.ManyToManyField(Autor) # Relação muito para muitos
    agencia = models.ForeignKey(Agencia) # Relação de chave estrangeira
    
    def __str__(self):
        return self.titulo
