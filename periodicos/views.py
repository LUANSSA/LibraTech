from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from .models import Periodicos
from django.contrib.auth.mixins import LoginRequiredMixin

# Listar periódicos
class PeriodicosListarView(ListView):
    # Modelo
    model = Periodicos
    # Arquivo
    template_name = "periodicos/periodicos_listar.html"
    # Nome do modelo
    context_object_name = "periodicos"
    # Quantidade de itens por página
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search", "")

        queryset = queryset.filter(
            Q(titulo__icontains=search) |
            Q(sub_titulo__icontains=search) |
            Q(assunto__icontains=search) |
            Q(area_acervo__icontains=search)
        )
        return queryset

# Detalhe de periódicos
class PeriodicosDetalheView(DetailView):
    # Modelo
    model = Periodicos
    # Arquivo
    template_name = "periodicos/periodicos_detalhe.html"
    # Nome do modelo
    context_object_name = "periodicos"

# Cadastrar periódico
class PeriodicosCadastrarView(LoginRequiredMixin, CreateView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
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
class PeriodicosAlterarView(LoginRequiredMixin, UpdateView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
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

# Excluir periódico
class PeriodicosExcluirView(LoginRequiredMixin, DeleteView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = Periodicos
    # Arquivo
    template_name = "periodicos/periodicos_excluir.html"
    # Nome do modelo
    context_object_name = "periodicos"
    # Redirecionar
    success_url = "/periodicos"
