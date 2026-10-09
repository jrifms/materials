# disciplines/admin.py

from django.contrib import admin
from .models import Nivel, Disciplina, Conteudo, Atividades


@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivel")
    list_filter = ("nivel",)


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "disciplina")
    list_filter = ("disciplina",)
    search_fields = ("titulo", "disciplina__nome")


@admin.register(Atividades)
class AtividadesAdmin(admin.ModelAdmin):
    list_display = ("conteudo",)
    list_filter = ("conteudo__disciplina",)