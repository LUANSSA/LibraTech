from django.shortcuts import render

# Create your views here.


# Listar arquivos
def ArquivosListarView(request):
    return render(request, "arquivos/arquivos_listar.html")

# Cadastrar arquivos
# def ArquivosCadastrarView(request):
#     render(request, "arquivos_cadastrar.html")

# # Alterar arquivos
# def ArquivosAlterarView(request):
#     render(request, "arquivos_alterar")

# # Excluir arquivos
# def ArquivosExcluirView(request):
#     render(request, "arquivos_excluir.html")