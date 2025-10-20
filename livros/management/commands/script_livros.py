from django.core.management.base import BaseCommand
from livros.models import Livros
from datetime import date
import random

class Command(BaseCommand):
    help = "Popula o tabela de livros"

    def handle(self, *args, **kwargs):
        # Evita duplicar registros
        # if (Livros.objects.exists()):
        #     self.stdout.write(self.style.WARNING("⚠️  Já existem livros cadastrados. Nenhum dado inserido."))
        
        livros = [
            {
                "titulo": "Introdução à Programação com Python",
                "sub_titulo": "Conceitos, algoritmos e boas práticas",
                "colecao": "Tecnologia e Desenvolvimento",
                "descricao": "Um guia completo para iniciantes que desejam aprender programação usando Python.",
                "edicao": "3ª",
                "local": "São Paulo",
                "editora": "Novatec",
                "ano": 2021,
                "mes_ano_publicacao": date(2021, 5, 15),
                "paginas": 350,
                "volume": "1",
                "tomo": "A",
                "chamada": "005.13 P974",
                "num_tombamento": "LT-0001",
                "assunto": "Programação",
                "area_acervo": "Tecnologia",
                "referencia_ABNT": "SOUZA, L. Introdução à Programação com Python. 3. ed. São Paulo: Novatec, 2021.",
                "nota": "Excelente para iniciantes.",
            },
            {
                "titulo": "Banco de Dados Relacionais",
                "sub_titulo": "Modelagem e SQL avançado",
                "colecao": "Engenharia de Software",
                "descricao": "Aborda a modelagem de dados e o uso de SQL em sistemas corporativos.",
                "edicao": "2ª",
                "local": "Rio de Janeiro",
                "editora": "Alta Books",
                "ano": 2020,
                "mes_ano_publicacao": date(2020, 8, 10),
                "paginas": 412,
                "volume": "1",
                "tomo": "B",
                "chamada": "005.74 B215",
                "num_tombamento": "LT-0002",
                "assunto": "Banco de Dados",
                "area_acervo": "Tecnologia",
                "referencia_ABNT": "PEREIRA, J. Banco de Dados Relacionais. 2. ed. Rio de Janeiro: Alta Books, 2020.",
                "nota": "Inclui exercícios práticos.",
            },
            {
                "titulo": "História da Computação",
                "sub_titulo": "Das primeiras máquinas ao século XXI",
                "colecao": "História da Tecnologia",
                "descricao": "Uma jornada pelos marcos da evolução dos computadores e da tecnologia digital.",
                "edicao": "1ª",
                "local": "Curitiba",
                "editora": "Editora UFPR",
                "ano": 2018,
                "mes_ano_publicacao": date(2018, 3, 22),
                "paginas": 280,
                "volume": "1",
                "tomo": "C",
                "chamada": "004.09 H675",
                "num_tombamento": "LT-0003",
                "assunto": "História da Computação",
                "area_acervo": "Ciência e Tecnologia",
                "referencia_ABNT": "MARTINS, R. História da Computação. 1. ed. Curitiba: UFPR, 2018.",
                "nota": "Com ilustrações raras.",
            },
            {
                "titulo": "Redes de Computadores",
                "sub_titulo": "Fundamentos e práticas modernas",
                "colecao": "Engenharia de Redes",
                "descricao": "Cobre os principais protocolos, arquiteturas e ferramentas de rede.",
                "edicao": "6ª",
                "local": "Porto Alegre",
                "editora": "Bookman",
                "ano": 2022,
                "mes_ano_publicacao": date(2022, 7, 5),
                "paginas": 540,
                "volume": "2",
                "tomo": "A",
                "chamada": "004.6 R324",
                "num_tombamento": "LT-0004",
                "assunto": "Redes",
                "area_acervo": "Tecnologia da Informação",
                "referencia_ABNT": "CASTRO, P. Redes de Computadores. 6. ed. Porto Alegre: Bookman, 2022.",
                "nota": "Abrange IPv6 e redes sem fio.",
            },
            {
                "titulo": "Engenharia de Software Moderna",
                "sub_titulo": "Princípios e práticas ágeis",
                "colecao": "Desenvolvimento de Sistemas",
                "descricao": "Explora as principais metodologias e práticas ágeis aplicadas ao desenvolvimento de software.",
                "edicao": "4ª",
                "local": "São Paulo",
                "editora": "Pearson",
                "ano": 2023,
                "mes_ano_publicacao": date(2023, 2, 1),
                "paginas": 610,
                "volume": "1",
                "tomo": "D",
                "chamada": "005.1 E573",
                "num_tombamento": "LT-0005",
                "assunto": "Engenharia de Software",
                "area_acervo": "Computação",
                "referencia_ABNT": "COSTA, F. Engenharia de Software Moderna. 4. ed. São Paulo: Pearson, 2023.",
                "nota": "Baseado no Manifesto Ágil.",
            },
        ]

        # Gera os livros restantes (6–20)
        for i in range(6, 21):
            livros.append({
                "titulo": f"Livro Técnico {i}",
                "sub_titulo": f"Subtítulo do Livro {i}",
                "colecao": f"Coleção Saber {random.choice(['A', 'B', 'C'])}",
                "descricao": f"Descrição fictícia do livro técnico número {i}, abordando conceitos variados.",
                "edicao": f"{random.randint(1,5)}ª",
                "local": random.choice(["São Paulo", "Rio de Janeiro", "Salvador", "Recife", "Porto Alegre"]),
                "editora": random.choice(["Editora Atlas", "Alta Books", "Bookman", "Pearson", "Novatec"]),
                "ano": random.randint(2015, 2024),
                "mes_ano_publicacao": date(random.randint(2015, 2024), random.randint(1, 12), random.randint(1, 28)),
                "paginas": random.randint(150, 800),
                "volume": str(random.randint(1, 3)),
                "tomo": random.choice(["A", "B", "C"]),
                "chamada": f"00{i}.T{i} L{i}",
                "num_tombamento": f"LT-{i:04d}",
                "assunto": random.choice(["Ciência da Computação", "Linguagens de Programação", "Banco de Dados", "Redes", "Engenharia de Software"]),
                "area_acervo": random.choice(["Tecnologia", "Computação", "Sistemas de Informação"]),
                "referencia_ABNT": f"AUTOR {i}. Livro Técnico {i}. {random.randint(1,5)}. ed. {random.choice(['São Paulo', 'Rio de Janeiro'])}: {random.choice(['Atlas', 'Pearson', 'Bookman'])}, {random.randint(2016, 2024)}.",
                "nota": f"Nota fictícia do livro {i}.",
            })


        for livro in livros:
            Livros.objects.create(**livro)
        
        self.stdout.write(self.style.SUCCESS("✅ livros criados com sucesso!"))