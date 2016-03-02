from __future__ import unicode_literals

from django.db import models

class Pessoa(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    comment = models.CharField(max_length=400)

class Key(models.Model):
    user = models.ForeignKey(Pessoa)
    data = models.CharField(max_length=30)
