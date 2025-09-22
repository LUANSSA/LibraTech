from django.shortcuts import render

# Create your views here.

def RevistasListarView(request):
    return render(request, "revistas/revistas_listar.html")