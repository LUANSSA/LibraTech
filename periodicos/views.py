from django.shortcuts import render

# Create your views here.


# Listar periódico
def PeriodicosListarView(request):
    return render(request, "periodicos/periodicos_listar.html")

# Cadastrar periódico
# def PeriodicosCadastrarView(request):
#     return render(request, "periodicos/periodicos_cadastrar.html")

# # Alterar periódico
# def PeriodicosAlterarView(request):
#     return render(request, "periodicos/periodicos_alterar.html")

# # Excluir periódico
# def PeriodicoExcluirView(request):
#     return render(request, "periodico/periodico_excluir.html")