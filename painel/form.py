from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Formulário de cadastro de usuário
class PainelUsuariosCadastrarFrom(UserCreationForm):
    # E-mail
    email = forms.EmailField(required=True)
    # Nome completo
    nome_completo = forms.CharField(required=True, label="Nome completo")

    class Meta:
        model = User
        # Campos do formulário
        fields = ["nome_completo", "email", "password1", "password2"]

    # Salvar usuário
    def save(self, commit=True):
        user = super().save(commit=False)

        # username recebe o email
        user.username = self.cleaned_data["email"]

        # Nome completo no first_name
        user.first_name = self.cleaned_data["nome_completo"]
        # E-mail
        user.email = self.cleaned_data["email"]

        # Salva
        if commit:
            user.save()

        return user



class PainelEntrarEmailForm(AuthenticationForm):
    username = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'autofocus': True}))