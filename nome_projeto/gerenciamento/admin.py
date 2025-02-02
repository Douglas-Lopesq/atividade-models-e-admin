from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'preco', 'quantidade', 'data_criacao')
    search_fields = ('codigo', 'nome')
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)
