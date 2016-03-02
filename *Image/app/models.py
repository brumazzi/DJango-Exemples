from __future__ import unicode_literals

from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=60)
    file = models.ImageField(null=True)
