from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    list_per_page = 10
    search_fields = ('nome',)
    

admin.site.register(Pessoa, ListandoPessoas)
