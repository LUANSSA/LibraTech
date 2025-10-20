from django.core.management.base import BaseCommand
from periodicos.models import Periodicos
from datetime import date
import random

class Command(BaseCommand):
    help = "Popula a tabela de periódicos"

    def handle(self, *args, **kwargs):
        # Evita duplicar registros
        # if Periodicos.objects.exists():
        #     self.stdout.write(self.style.WARNING("⚠️  Já existem periódicos cadastrados. Nenhum dado inserido."))
        #     return

        periodicos = [
            {
                "titulo": "Revista Brasileira de Computação Aplicada",
                "sub_titulo": "Tecnologias e Inovações",
                "issn": "2238-4217",
                "frequencia": "Trimestral",
                "periodo_inicio": date(2010, 3, 1),
                "periodo_fim": None,
                "volume": "15",
                "numero": "2",
                "editora": "Sociedade Brasileira de Computação",
                "local": "Porto Alegre",
                "assunto": "Computação Aplicada",
                "area_acervo": "Tecnologia da Informação",
                "referencia_ABNT": "REVISTA BRASILEIRA DE COMPUTAÇÃO APLICADA. Porto Alegre: SBC, v.15, n.2, mar. 2024.",
                "nota": "Publicação reconhecida pela comunidade acadêmica de TI.",
                "disponibilidade": True,
            },
            {
                "titulo": "Revista de Engenharia de Software",
                "sub_titulo": "Práticas e Estudos de Caso",
                "issn": "1982-4363",
                "frequencia": "Semestral",
                "periodo_inicio": date(2008, 1, 1),
                "periodo_fim": None,
                "volume": "12",
                "numero": "1",
                "editora": "Universidade Federal de Pernambuco",
                "local": "Recife",
                "assunto": "Engenharia de Software",
                "area_acervo": "Computação",
                "referencia_ABNT": "REVISTA DE ENGENHARIA DE SOFTWARE. Recife: UFPE, v.12, n.1, jan./jun. 2023.",
                "nota": "Foco em metodologias ágeis e gestão de projetos.",
                "disponibilidade": True,
            },
            {
                "titulo": "Ciência da Informação",
                "sub_titulo": "Teoria e Prática",
                "issn": "0100-1965",
                "frequencia": "Quadrimestral",
                "periodo_inicio": date(1972, 5, 1),
                "periodo_fim": None,
                "volume": "52",
                "numero": "3",
                "editora": "IBICT",
                "local": "Brasília",
                "assunto": "Gestão da Informação",
                "area_acervo": "Ciência da Informação",
                "referencia_ABNT": "CIÊNCIA DA INFORMAÇÃO. Brasília: IBICT, v.52, n.3, maio/ago. 2024.",
                "nota": "Publicação consolidada na área de biblioteconomia e TI.",
                "disponibilidade": True,
            },
            {
                "titulo": "Revista Eletrônica de Sistemas de Informação",
                "sub_titulo": "Perspectivas e Tendências",
                "issn": "1677-3071",
                "frequencia": "Trimestral",
                "periodo_inicio": date(2002, 4, 1),
                "periodo_fim": None,
                "volume": "23",
                "numero": "4",
                "editora": "UFSC",
                "local": "Florianópolis",
                "assunto": "Sistemas de Informação",
                "area_acervo": "Tecnologia da Informação",
                "referencia_ABNT": "REVISTA ELETRÔNICA DE SISTEMAS DE INFORMAÇÃO. Florianópolis: UFSC, v.23, n.4, out./dez. 2024.",
                "nota": "Disponível integralmente online.",
                "disponibilidade": True,
            },
            {
                "titulo": "Boletim Técnico da Embrapa Informática Agropecuária",
                "sub_titulo": "Avanços Tecnológicos no Agronegócio",
                "issn": "1517-310X",
                "frequencia": "Anual",
                "periodo_inicio": date(1995, 1, 1),
                "periodo_fim": None,
                "volume": "28",
                "numero": "1",
                "editora": "Embrapa",
                "local": "Campinas",
                "assunto": "Informática Agropecuária",
                "area_acervo": "Tecnologia e Agricultura",
                "referencia_ABNT": "BOLETIM TÉCNICO DA EMBRAPA INFORMÁTICA AGROPECUÁRIA. Campinas: Embrapa, v.28, n.1, 2023.",
                "nota": "Inclui estudos sobre IA aplicada ao agronegócio.",
                "disponibilidade": True,
            },
        ]

        # Gera registros fictícios adicionais (6–20)
        for i in range(6, 21):
            periodicos.append({
                "titulo": f"Revista Técnica {i}",
                "sub_titulo": f"Edição Especial {i}",
                "issn": f"9999-10{i:02d}",
                "frequencia": random.choice(["Mensal", "Bimestral", "Trimestral", "Semestral"]),
                "periodo_inicio": date(random.randint(2000, 2023), random.randint(1, 12), 1),
                "periodo_fim": None,
                "volume": str(random.randint(1, 30)),
                "numero": str(random.randint(1, 6)),
                "editora": random.choice(["Editora Atlas", "Bookman", "Pearson", "UFBA", "UFSC"]),
                "local": random.choice(["São Paulo", "Rio de Janeiro", "Salvador", "Curitiba", "Brasília"]),
                "assunto": random.choice(["Computação", "Engenharia", "Gestão da Informação", "Educação Tecnológica"]),
                "area_acervo": random.choice(["Tecnologia", "Educação", "Informação", "Engenharia"]),
                "referencia_ABNT": f"REVISTA TÉCNICA {i}. {random.choice(['São Paulo', 'Recife', 'Salvador'])}: {random.choice(['Atlas', 'UFPE', 'UFBA'])}, v.{random.randint(1, 20)}, n.{random.randint(1, 6)}, {random.randint(2015, 2024)}.",
                "nota": f"Edição fictícia gerada automaticamente ({i}).",
                "disponibilidade": True,
            })

        for periodico in periodicos:
            Periodicos.objects.create(**periodico)

        self.stdout.write(self.style.SUCCESS("✅ Periódicos criados com sucesso!"))
