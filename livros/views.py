from django.shortcuts import render
from django.http import HttpResponse
# from models import Livros
# Create your views here.


# Listar livros
def LivoListarView(request):
    return render(request, "livros/livros_listar.html")

# # Cadastrar/Alterar livro
# def LivroCadastrarView(request):
#     return (request, "templates/livros/livros_cadastrar.html")

# # Alterar livro
# def LivroAlterarView(request):
#     return (request, "templates/livros/livros_alterar.html")

# # Excluir livro
# def LivroExcluirView(request):
#     return(request, "templates/livros/livros_excluir.html")
