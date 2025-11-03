from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

# from models import Livros
# Create your views here.

from .models import Arquivos

# Listar arquivos
class ArquivosListarView(ListView):
    # Modelo
    model = Arquivos
    # Arquivo
    template_name = "arquivos/arquivos_listar.html"
    # Nome do modelo
    context_object_name = "arquivos"
    # Quantidade de itens por página
    paginate_by = 8

    # Consulta com filtro
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search", "")

        queryset = queryset.filter(
            Q(titulo__icontains=search) |
            Q(descricao__icontains=search) |
            Q(tipo_arquivo__icontains=search)

        ).order_by("id")
        return queryset
    
# Detalhe de arquivo
class ArquivosDetalheView(DetailView):
    # Modelo
    model = Arquivos
    # Arquivo
    template_name = "arquivos/arquivos_detalhe.html"
    # Nome do modelo
    context_object_name = "arquivos"

# Cadastrar arquivo
class ArquivosCadastrarView(LoginRequiredMixin, CreateView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = Arquivos
    # Arquivo
    template_name = "arquivos/arquivos_form.html"
    # Nome do modelo
    context_object_name = "arquivos"
    # Formulário
    fields = [
        "titulo", "descricao", "colecao", "tipo_arquivo", "arquivo", "autor",
        "data_publicacao", "assunto", "area_acervo", "chamada", "num_tombamento",
        "referencia_ABNT", "nota", "disponibilidade",
    ]
    # Redirecionar após cadastro
    success_url = "/painel/arquivos/"

# Alterar arquivo
class ArquivosAlterarView(LoginRequiredMixin, UpdateView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = Arquivos
    # Arquivo
    template_name = "arquivos/arquivos_form.html"
    # Nome do modelo
    context_object_name = "arquivos"
    # Formulário
    fields = [
        "titulo", "descricao", "tipo_arquivo", "arquivo_upload"
    ]
    # Redirecionar após alteração
    success_url = "/painel/arquivos/"

# Excluir arquivo
class ArquivosExcluirView(LoginRequiredMixin, DeleteView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = Arquivos
    # Arquivo
    template_name = "arquivos/arquivos_confirm_delete.html"
    # Nome do modelo
    context_object_name = "arquivos"
    # Redirecionar após exclusão
    success_url = "/painel/arquivos/"


