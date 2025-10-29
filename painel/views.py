from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .form import PainelUsuariosCadastrarFrom

# Models
from django.contrib.auth.models import User
from livros.models import Livros
from revistas.models import Revistas
from periodicos.models import Periodicos
from arquivos.models import Arquivos


# Painel dashboard
class PainelDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "painel/painel_dashboard.html"
    login_url = "painel_entrar"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Total de cada entidade para os cards
        context["total_usuarios"] = User.objects.count()
        context["total_livros"] = Livros.objects.count()
        context["total_periodicos"] = Periodicos.objects.count()
        context["total_revistas"] = Revistas.objects.count()
        context["total_arquivos"] = Arquivos.objects.count()

        return context

# Painel Listar usuários
class PainlDashboardUsuariosListarView(LoginRequiredMixin, ListView):
    model = User
    template_name = "painel/painel_dashboard_usuarios_listar.html"
    context_object_name = "usuarios"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Total de cada entidade para os cards
        context["total_usuarios"] = User.objects.count()

        return context

# Cadastrar usuários
class PainelUsuariosCadastrarView(CreateView):
    model = User
    form_class = PainelUsuariosCadastrarFrom
    template_name = "painel/painel_usuarios_form.html"
    success_url = reverse_lazy("painel_entrar")

    def form_valid(self, form):
        response = super().form_valid(form)
        # adiciona a mensagem de sucesso
        messages.success(self.request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return response

# Painel login
class PainelEntrarView(LoginView):
    template_name = "painel/painel_entrar.html"
    redirect_authenticated_user = True  # já redireciona usuários logados automaticamente

    # Redireciona para página de dashboard
    def get_success_url(self):
        return reverse_lazy("painel_dashboard")

    # Mensagem caso login falhe
    def form_invalid(self, form):
        messages.error(self.request, "Usuário ou senha incorretos.")
        return super().form_invalid(form)

# Painel recuperar senha
class PainelRecuperarSenhaView(PasswordResetView):
    template_name = "painel/painel_recuperar_senha.html"
    email_template_name = "painel/emails/reset_password_email.html"
    success_url = reverse_lazy("painel_entrar")

# Painel redefinir senha (após o link enviado por e-mail)
class PainelRedefinirSenhaView(LoginView):
    template_name = "painel/painel_redefinir_senha.html"
    success_url = reverse_lazy("painel_entrar")

# Painel sair da conta
class PainelSairView(LogoutView):
    next_page = "painel_entrar"  # redireciona para login após logout
