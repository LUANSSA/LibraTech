from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .form import PainelUsuariosCadastrarFrom, PainelEntrarEmailForm
from django.db.models import Q

# Models
from django.contrib.auth.models import User
from livros.models import Livros
from revistas.models import Revistas
from periodicos.models import Periodicos
from arquivos.models import Arquivos

# ========== PAINEL ==========

# Painel dashboard
class PainelDashboardView(LoginRequiredMixin, TemplateView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    template_name = "painel/painel_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Total de cada entidade para os cards
        context["total_usuarios"] = User.objects.count()
        context["total_livros"] = Livros.objects.count()
        context["total_periodicos"] = Periodicos.objects.count()
        context["total_revistas"] = Revistas.objects.count()
        context["total_arquivos"] = Arquivos.objects.count()

        return context
    

    
# Painel dashboard cadastrar usuários
class PainelDashboardUsuariosCadastrarView(LoginRequiredMixin, CreateView):
    login_url = "painel_site_entrar"
    model = User
    # Define como deve funcionar a classe form
    form_class = PainelUsuariosCadastrarFrom
    # Arquivo
    template_name = "painel/painel_dashboard_usuarios_form.html"

    def form_valid(self, form):
        user = form.save()
        # Mensagem
        messages.success(self.request,"Cadastro realizado com sucesso!")
        return super().form_valid(form)

    success_url = reverse_lazy("painel_dashboard_usuarios_listar")

    
# Painel dashboard alterar usuários
class PainelDashboardUsuariosAlterarView(LoginRequiredMixin, UpdateView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    model = User
    form_class = PainelUsuariosCadastrarFrom
    template_name = "painel/painel_dashboard_usuarios_form.html"

    def form_valid(self, form):
        # Quando o formulário for válido, realiza a atualização
        response = super().form_valid(form)
        messages.success(self.request, "Usuário alterado com sucesso!")
        return response
    
    def get_success_url(self):
        # Define para onde redirecionar após o sucesso
        return reverse_lazy("painel_dashboard_usuarios_listar")
    
# Painel dashboard excluir usuários
class PainelDashboardUsuariosExcluirView(LoginRequiredMixin, DeleteView):
    model = User
    login_url = "painel_site_entrar"
    success_url = reverse_lazy("painel_dashboard_usuarios_listar")
    template_name = "painel/painel_dashboard_usuarios_excluir.html"
     # Nome do modelo
    context_object_name = "usuarios"
 
# Painel dashboard listar usuários
class PainlDashboardUsuariosListarView(LoginRequiredMixin, ListView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Modelo
    model = User
    # Arquivo
    template_name = "painel/painel_dashboard_usuarios_listar.html"
    # Nome do modelo
    context_object_name = "usuarios"
     # Quantidade de itens por página
    paginate_by = 8

    # Consulta com filtro
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search", "")
        
        queryset = queryset.filter(
            Q(first_name__icontains=search) |
            Q(email__icontains=search) | 
            Q(groups__name__icontains=search)

        ).order_by("id")

        return queryset
    
# Painel sair da conta
class PainelSairView(LoginRequiredMixin, LogoutView):
    # Redireciona para login caso não esteja autenticado
    login_url = "painel_site_entrar"
    # Define para onde redirecionar após o logout
    next_page = "painel_site_entrar"  # redireciona para login após logout


# ========== SITE ==========

# Painel site cadastrar usuários
class PainelSiteUsuariosCadastrarView(CreateView):
    model = User
    form_class = PainelUsuariosCadastrarFrom
    template_name = "painel/painel_site_usuarios_form.html"
    success_url = reverse_lazy("painel_site_entrar")

    def form_valid(self, form):
        response = super().form_valid(form)
        # adiciona a mensagem de sucesso
        messages.success(self.request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return response

# Painel site Entrar
class PainelSiteEntrarView(LoginView):
    template_name = "painel/painel_site_entrar.html"
    redirect_authenticated_user = True  # já redireciona usuários logados automaticamente
    authentication_form = PainelEntrarEmailForm

    # Redirecionar
    def get_success_url(self):
        return reverse_lazy("painel_dashboard")

    # Mensagem caso login falhe
    def form_invalid(self, form):
        messages.error(self.request, "Usuário ou senha incorretos.")
        return super().form_invalid(form)

# Painel site recuperar senha
class PainelSiteRecuperarSenhaView(PasswordResetView):
    template_name = "painel/painel_site_recuperar_senha.html"
    email_template_name = "painel/emails/reset_password_email.html"

    # Redirecionar
    def get_success_url(self):
        return reverse_lazy("painel_site_entrar")

# Painel site redefinir senha (após o link enviado por e-mail)
class PainelSiteRedefinirSenhaView(LoginView):
    template_name = "painel/painel_redefinir_senha.html"
    
    # Redirecionar
    def get_success_url(self):
        return reverse_lazy("painel_site_entrar")
