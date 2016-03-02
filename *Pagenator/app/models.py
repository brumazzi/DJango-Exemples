from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField('Title', max_length=100)
    content = models.TextField('Content')
    author = models.CharField('Author', max_length=80)

    def __str__(self):
        return self.title
