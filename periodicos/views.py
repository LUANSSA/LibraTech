from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Periodicos

# Listar periódicos
class PeriodicosListarView(ListView):
    model = Periodicos
    template_name = "periodicos/periodicos_listar.html"
    context_object_name = "periodicos"

# Cadastrar periódico
class PeriodicosCadastrarView(CreateView):
    # Modelo
    model = Periodicos
    # Arquivo
    template_name = "periodicos/periodicos_form.html"
    # Nome do modelo
    context_object_name = "periodicos"
    fields = [
        "titulo", "sub_titulo", "issn", "frequencia", "periodo_inicio", "periodo_fim",
        "volume", "numero", "editora", "local", "assunto", "area_acervo",
        "referencia_ABNT", "nota", "disponibilidade"
    ]
    # Redirecionar
    success_url = "/periodicos"

# Alterar periódico
class PeriodicosAlterarView(UpdateView):
    # Modelo
    model = Periodicos
    # Arquivo
    template_name = "periodicos/periodicos_form.html"
    # Nome do modelo
    context_object_name = "periodicos"
    fields = [
        "titulo", "sub_titulo", "issn", "frequencia", "periodo_inicio", "periodo_fim",
        "volume", "numero", "editora", "local", "assunto", "area_acervo",
        "referencia_ABNT", "nota", "disponibilidade"
    ]
    # Redirecionar
    success_url = "/periodicos"

class PeriodicosExcluirView(DeleteView):
    # Modelo
    model = Periodicos
    # Arquivo
    template_name = "periodicos/periodicos_excluir.html"
    # Nome do modelo
    context_object_name = "periodicos"
    # Redirecionar
    success_url = "/periodicos"
