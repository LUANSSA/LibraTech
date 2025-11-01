from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

# from models import Livros
# Create your views here.

from .models import Livros

# Listar livros
class LivrosListarView(ListView):
    # Modelo
    model = Livros
    # Arquivo
    template_name = "livros/livros_listar.html"
    # Nome do modelo
    context_object_name = "livros"
    # Quantidade de itens por página
    paginate_by = 8

    # Consulta com filtro
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search", "")

        queryset = queryset.filter(
            Q(titulo__icontains=search) |
            Q(sub_titulo__icontains=search) |
            Q(area_acervo__icontains=search) |
            Q(assunto__icontains=search)

        )
        return queryset
    
# Detalhe de livro
class LivrosDetalheView(DetailView):
    # Modelo
    model = Livros
    # Arquivo
    template_name = "livros/livros_detalhe.html"
    # Nome do modelo
    context_object_name = "livros"

# Cadastrar livro
class LivrosCadastrarView(LoginRequiredMixin, CreateView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = Livros
    # Arquivo
    template_name = "livros/livros_form.html"
    # Nome do modelo
    context_object_name = "livros"
    # Formulário
    fields = [
        "titulo", "sub_titulo", "colecao", "descricao", "edicao",
        "local", "editora", "ano", "mes_ano_publicacao", "paginas",
        "volume", "tomo", "chamada", "num_tombamento", "assunto",
        "area_acervo", "referencia_ABNT", "nota", "disponibilidade"
    ]
    # Redirecionar
    success_url = "/livros"

# Alterar livro
class LivrosAlterarView(LoginRequiredMixin, UpdateView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = Livros
     # Arquivo
    template_name = "livros/livros_form.html"
    # Nome do modelo
    context_object_name = "livros"
    # Formulário
    fields = [
        "titulo", "sub_titulo", "colecao", "descricao", "edicao",
        "local", "editora", "ano", "mes_ano_publicacao", "paginas",
        "volume", "tomo", "chamada", "num_tombamento", "assunto",
        "area_acervo", "referencia_ABNT", "nota", "disponibilidade"
    ]
    # Redirecionar
    success_url = "/livros"

# Excluir livro
class LivrosExcluirView(LoginRequiredMixin, DeleteView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = Livros
    # Arquivo
    template_name = "livros/livros_excluir.html"
    # Nome do modelo
    context_object_name = "livros"
    # Redirecionar
    success_url = "/livros"
