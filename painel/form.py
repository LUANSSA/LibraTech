from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group

# Formulário de cadastro e alteração de usuário no painel
class PainelUsuariosCadastrarFrom(UserCreationForm):
    # E-mail
    email = forms.EmailField(required=True)
    # Nome completo
    nome_completo = forms.CharField(required=True, label="Nome completo")

    # Grupos de usuários
    groups = forms.ModelChoiceField(
        queryset=Group.objects.filter(name__in=["Administrador", "Visitante"]),
        label="Grupo do usuário",
        required=True,
        empty_label="Selecione um grupo"
    )

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

            # Atualiza grupo
            user.groups.clear()
            user.groups.add(self.cleaned_data["groups"])

        return user

class PainelEntrarEmailForm(AuthenticationForm):
    username = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'autofocus': True}))

    # Formulário de cadastro de usuario no site
class SiteUsuariosCadastrarFrom(UserCreationForm):
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
            
            # Adiciona grupo visitante caso usuário não tenha grupo
            if user.groups.count() == 0:
                grupo_visitante, criado = Group.objects.get_or_create(name="Visitante")
                user.groups.add(grupo_visitante)

        return user