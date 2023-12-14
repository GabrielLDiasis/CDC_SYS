from django.contrib import admin
from contabil.models import CalculoRecisorio as CalculoRecisorioModel, Projeto as ProjetoModel, Provisao as ProvisaoModel, Trabalhador as TrabalhadorModel

class CalculoRecisorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'admissao', 'demissao', 'salario_bruto')
    search_fields = ('nome', 'cpf')
    list_filter = ('admissao', 'demissao')

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'saldo_inicial', 'data_inicio', 'data_fim')
    search_fields = ('nome',)
    list_filter = ('data_inicio', 'data_fim')

class ProvisaoAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'saldo', 'rubrica', 'categoria', 'subcategoria')
    search_fields = ('projeto', 'rubrica')
    list_filter = ('categoria', 'subcategoria')

class TrabalhadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cidade', 'estado')
    search_fields = ('nome', 'cpf', 'cidade')
    list_filter = ('cidade', 'estado')

admin.site.register(CalculoRecisorioModel, CalculoRecisorioAdmin)
admin.site.register(ProjetoModel, ProjetoAdmin)
admin.site.register(ProvisaoModel, ProvisaoAdmin)
admin.site.register(TrabalhadorModel, TrabalhadorAdmin)