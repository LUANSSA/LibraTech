from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Cria os grupos de usuários do sistema"

    def handle(self, *args, **kwargs):
        grupos = [
            "Diretor",
            "Administrador",
            "Visitante"
        ]

        for nome in grupos:
            criado = Group.objects.get_or_create(name=nome)
            if criado:
                self.stdout.write(self.style.SUCCESS(f"Grupo criado: {nome}"))
            else:
                self.stdout.write(f"Grupo já existe: {nome}")

        self.stdout.write(self.style.SUCCESS("Todos os grupos foram configurados!"))
