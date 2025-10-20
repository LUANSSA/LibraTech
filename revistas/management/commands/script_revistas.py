from django.core.management.base import BaseCommand
from revistas.models import Revistas
from datetime import date
import random

class Command(BaseCommand):
    help = "Popula a tabela de revistas com dados fictícios"

    def handle(self, *args, **kwargs):
        revistas = [
            {
                "titulo": "Revista Brasileira de Tecnologia",
                "sub_titulo": "Inovações e Tendências",
                "issn": "2238-9876",
                "edicao": "12",
                "volume": "5",
                "numero": "2",
                "data_publicacao": date(2024, 3, 1),
                "local": "São Paulo",
                "editora": "Editora Atlas",
                "paginas": 120,
                "colecao": "Tecnologia",
                "assunto": "Computação e Inovação",
                "area_acervo": "Tecnologia da Informação",
                "chamada": "TEC-001",
                "num_tombamento": "1001",
                "descricao": "Revista focada em tecnologias aplicadas e inovação.",
                "referencia_ABNT": "REVISTA BRASILEIRA DE TECNOLOGIA. São Paulo: Atlas, v.5, n.2, mar. 2024.",
                "nota": "Edição anual com artigos acadêmicos.",
                "disponibilidade": True,
            },
            {
                "titulo": "Revista Científica de Engenharia",
                "sub_titulo": "Estudos e Pesquisas",
                "issn": "1987-6543",
                "edicao": "8",
                "volume": "3",
                "numero": "1",
                "data_publicacao": date(2023, 6, 15),
                "local": "Rio de Janeiro",
                "editora": "Editora UFJR",
                "paginas": 90,
                "colecao": "Engenharia",
                "assunto": "Engenharia Civil",
                "area_acervo": "Engenharia",
                "chamada": "ENG-002",
                "num_tombamento": "1002",
                "descricao": "Revista voltada para pesquisas em engenharia civil.",
                "referencia_ABNT": "REVISTA CIENTÍFICA DE ENGENHARIA. Rio de Janeiro: UFJR, v.3, n.1, jun. 2023.",
                "nota": "Inclui estudos sobre sustentabilidade e estruturas.",
                "disponibilidade": True,
            },
        ]

        # Gera registros fictícios adicionais (3–10)
        for i in range(3, 11):
            revistas.append({
                "titulo": f"Revista Técnica {i}",
                "sub_titulo": f"Edição Especial {i}",
                "issn": f"9999-20{i:02d}",
                "edicao": str(random.randint(1, 15)),
                "volume": str(random.randint(1, 10)),
                "numero": str(random.randint(1, 4)),
                "data_publicacao": date(random.randint(2015, 2024), random.randint(1, 12), random.randint(1, 28)),
                "local": random.choice(["São Paulo", "Rio de Janeiro", "Salvador", "Curitiba", "Brasília"]),
                "editora": random.choice(["Atlas", "Pearson", "UFBA", "UFSC"]),
                "paginas": random.randint(50, 200),
                "colecao": random.choice(["Tecnologia", "Engenharia", "Educação"]),
                "assunto": random.choice(["Computação", "Engenharia", "Gestão da Informação"]),
                "area_acervo": random.choice(["Tecnologia", "Engenharia", "Educação"]),
                "chamada": f"TCH-{i:03d}",
                "num_tombamento": str(1000 + i),
                "descricao": f"Edição fictícia gerada automaticamente ({i})",
                "referencia_ABNT": f"REVISTA TÉCNICA {i}. São Paulo: Atlas, v.{random.randint(1,10)}, n.{random.randint(1,4)}, {random.randint(2015, 2024)}.",
                "nota": f"Edição fictícia ({i})",
                "disponibilidade": True,
            })

        # Insere os dados no banco
        for revista in revistas:
            Revistas.objects.create(**revista)

        self.stdout.write(self.style.SUCCESS("✅ Revistas criadas com sucesso!"))
