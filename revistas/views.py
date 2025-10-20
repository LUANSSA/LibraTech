from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q

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
        )

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
class RevistasCadastrarView(CreateView):
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
class RevistasAlterarView(UpdateView):
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
class RevistasExcluirView(DeleteView):
    # Modelo
    model = Revistas
    # Arquivo
    template_name = "revistas/revistas_excluir.html"
    # Nome do modelo
    context_object_name = "revistas"
    # Redirecionar
    success_url = "/revistas"
