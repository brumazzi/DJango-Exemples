#*-* coding:utf-8 *-*
from django.contrib import admin

from app.models import *

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome','email')
    search_fields = ('nome','email')
    list_filter = ('nome',)
    ordering = ('nome',)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pub_date', 'agencia') # Campos visiveis
    search_fields = ('titulo', 'agencia') # Campos para busca
    list_filter = ('titulo','pub_date') # lista para filtrar informações
    ordering = ('-pub_date',) # ordena por data
    date_hierarchy = 'pub_date' # ordena consulta por data
    fields = ('titulo','url','pub_date','autores','agencia', 'conteudo') # lista dos capos
    prepopulated_fields = {'url':('titulo',)} # referencia url ao titulo
    filter_horizontal = ('autores',) # filtro para busca
    raw_id_fields = ('agencia',)

class AgenciaAdmin(admin.ModelAdmin):
    list_display = ('nome','site')
    search_fields = ('nome',)
    ordering = ('nome',)

# faz o registro das classes no modo admin
admin.site.register(Agencia, AgenciaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Artigo, ArtigoAdmin)
