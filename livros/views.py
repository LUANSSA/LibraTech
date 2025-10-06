from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from models import Livros
# Create your views here.

from .models import Livros

# Listar livros
class LivroListarView(ListView):
    # Modelo
    model = Livros
    # Arquivo
    template_name = "livros/livros_listar.html"
    # Nome do modelo
    context_object_name = "livros"


# Cadastrar livro
class LivroCadastrarView(CreateView):
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
class LivroAlterarView(UpdateView):
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
class LivrosExcluirView(DeleteView):
    # Modelo
    model = Livros
    # Arquivo
    template_name = "livros/livros_excluir.html"
    # Nome do modelo
    context_object_name = "livros"
    # Redirecionar
    success_url = "/livros"
