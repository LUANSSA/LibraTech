from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Painel login
class PainelLoginView(LoginView):
    template_name = 'painel/painel_login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('painel:dashboard')


# Painel recuperar senha
class PainelRecuperarSenhaView(PasswordResetView):
    template_name = 'painel/painel_recuperar_senha.html'
    email_template_name = 'painel/emails/reset_password_email.html'
    success_url = reverse_lazy('painel:login')


# Painel redefinir senha (após o link enviado por e-mail)
class PainelRedefinirSenhaView(PasswordResetConfirmView):
    template_name = 'painel/painel_redefinir_senha.html'
    success_url = reverse_lazy('painel:login')


# Painel dashboard
class PainelDashboardView(TemplateView):
    template_name = 'painel/painel_dashboard.html'


# Listar usuários
class UsuariosListarView(ListView):
    model = User
    template_name = 'painel/painel_usuarios_listar.html'
    context_object_name = 'usuarios'
