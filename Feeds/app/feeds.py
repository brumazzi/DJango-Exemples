#*-* coding: utf-8 *-*

from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from .models import Artigo

class ArtigoRss(Feed):
    title = "Ultimos artigos"
    link = '/'
    description = "Ultimos artigos do site Django Feeds"

    def items(self):
        return Artigo.objects.all()
    def item_title(self, artigo):
        return artigo.title
    def item_description(self, artigo):
        return artigo.content
    def item_link(self,artigo):
        return "%s" % artigo.url
