#*-* coding: utf-8 *-*
from __future__ import unicode_literals

from django.db import models

class Artigo(models.Model):
    title = models.CharField('Titulo:',max_length=60)
    date = models.DateTimeField('Data de publicação:')
    author = models.CharField('Conteído da página:',max_length=60)
    content = models.TextField()
    url = models.URLField('Url')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date'] # Ordena em modo decrescente
