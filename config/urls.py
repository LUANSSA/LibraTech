"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import Home
from livros.views import *
from arquivos.views import *
from periodicos.views import *
from revistas.views import *
from painel.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    # Painel (dashboard e controle de usuários personalizado)

    # Painel Dashboard
    path('painel/dashboard/usuarios/', PainlDashboardUsuariosListarView.as_view(), name="painel_dashboard_usuarios_listar"),
    path('painel/dashboard/usuarios/form', PainlDashboardUsuariosListarView.as_view(), name="painel_dashboard_usuarios_form"),
    path('painel/dashboard', PainelDashboardView.as_view(), name="painel_dashboard"),

    # Painel Usuários
    path('painel/usuarios/form/', PainelUsuariosCadastrarView.as_view(), name="painel_usuarios_cadastrar"),
    path('login/', PainelEntrarView.as_view(), name="painel_entrar"),
    path('logout/', PainelSairView.as_view(), name='painel_sair'),
    path('recuperar-senha/', PainelRecuperarSenhaView.as_view(), name="painel_recuperar_senha"),
    path('redefinir-senha/', PainelRedefinirSenhaView.as_view(), name="painel_redefinir_senha"),

    path("", Home),

   # Arquivos
    path("painel/arquivos/", ArquivosListarView.as_view(), name="arquivos_listar"),
    path("painel/arquivos/<int:pk>/", ArquivosDetalheView.as_view(), name="arquivos_detalhe"),
    path("painel/arquivos/form/", ArquivosCadastrarView.as_view(), name="arquivos_cadastrar"),
    path("painel/arquivos/form/<int:pk>/", ArquivosAlterarView.as_view(), name="arquivos_alterar"),
    path("painel/arquivos/excluir/<int:pk>/", ArquivosExcluirView.as_view(), name="arquivos_excluir"),

    # Livros
    path("painel/livros/", LivrosListarView.as_view(), name="livros_listar"),
    path("painel/livros/<int:pk>/", LivrosDetalheView.as_view(), name="livros_detalhe"),
    path("painel/livros/form/", LivrosCadastrarView.as_view(), name="livros_cadastrar"),
    path("painel/livros/form/<int:pk>/", LivrosAlterarView.as_view(), name="livros_alterar"),
    path("painel/livros/excluir/<int:pk>/", LivrosExcluirView.as_view(), name="livros_excluir"),

    # Periódicos
    path("painel/periodicos/", PeriodicosListarView.as_view(), name="periodicos_listar"),
    path("painel/periodicos/<int:pk>/", PeriodicosDetalheView.as_view(), name="periodicos_detalhe"),
    path("painel/periodicos/form/", PeriodicosCadastrarView.as_view(), name="periodicos_cadastrar"),
    path("painel/periodicos/form/<int:pk>/", PeriodicosAlterarView.as_view(), name="periodicos_alterar"),
    path("painel/periodicos/excluir/<int:pk>/", PeriodicosExcluirView.as_view(), name="periodicos_excluir"),
    
    # Revistas
    path("painel/revistas/", RevistasListarView.as_view(), name="revistas_listar"),
    path("painel/revistas/<int:pk>/", RevistasDetalheView.as_view(), name="revistas_detalhe"),
    path("painel/revistas/form/", RevistasCadastrarView.as_view(), name="revistas_cadastrar"),
    path("painel/revistas/form/<int:pk>/", RevistasAlterarView.as_view(), name="revistas_alterar"),
    path("painel/revistas/excluir/<int:pk>/", RevistasExcluirView.as_view(), name="revistas_excluir"),
]
