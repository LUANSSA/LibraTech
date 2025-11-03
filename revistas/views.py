from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .models import Revistas

class RevistasListarView(ListView):
    # Modelo
    model = Revistas
    # Arquivo
    template_name = "revistas/revistas_listar.html"
    # Nome do modelo
    context_object_name = "revistas"
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
        ).order_by("-id")

        return queryset
    
# Detalhe de revista
class RevistasDetalheView(DetailView):
    # Modelo
    model = Revistas
    # Arquivo
    template_name = "revistas/revistas_detalhe.html"
    # Nome do modelo
    context_object_name = "revistas"

# Cadastrar revista
class RevistasCadastrarView(LoginRequiredMixin, CreateView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = Revistas
    # Arquivo
    template_name = "revistas/revistas_form.html"
    # Nome do modelo
    context_object_name = "revistas"
    # Formulário
    fields = [
        "titulo", "sub_titulo", "issn", "edicao", "volume",
        "numero", "data_publicacao", "local", "editora", "paginas",
        "colecao", "assunto", "area_acervo", "chamada", "num_tombamento",
        "descricao", "referencia_ABNT", "nota", "disponibilidade"
    ]
    # Redirecionamentp
    success_url = "/revistas"

# Alterar revista
class RevistasAlterarView(LoginRequiredMixin, UpdateView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = Revistas
     # Arquivo
    template_name = "revistas/revistas_form.html"
    # Nome do modelo
    context_object_name = "revistas"
    # Formulário
    fields = [
        "titulo", "sub_titulo", "issn", "edicao", "volume",
        "numero", "data_publicacao", "local", "editora", "paginas",
        "colecao", "assunto", "area_acervo", "chamada", "num_tombamento",
        "descricao", "referencia_ABNT", "nota", "disponibilidade"
    ]
    # Redirecionar
    success_url = "/revistas"

# Excluir revista
class RevistasExcluirView(LoginRequiredMixin, DeleteView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = Revistas
    # Arquivo
    template_name = "revistas/revistas_excluir.html"
    # Nome do modelo
    context_object_name = "revistas"
    # Redirecionar
    success_url = "/revistas"
