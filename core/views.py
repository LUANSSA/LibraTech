from django.views.generic import ListView
from django.db.models import Q
from livros.models import Livros
from periodicos.models import Periodicos
from revistas.models import Revistas

class Home(ListView):
    # Arquivo
    template_name = "core/home.html"
    # Nome do modelo
    context_object_name = "itens"
    # Quantidade de itens por página
    paginate_by = 9  # Limite de 9 itens por página

    def get_queryset(self):
        # Parâmetro
        search = self.request.GET.get("search", "").strip()

        # Nenhum item será exibido se não houver pesquisa
        if not search:
            return []

        # Consulta limitada a 3 de cada tipo
        livros = Livros.objects.filter(
            Q(titulo__icontains=search) |
            Q(sub_titulo__icontains=search) |
            Q(area_acervo__icontains=search) |
            Q(assunto__icontains=search)
        ).order_by("id")[:3]

        periodicos = Periodicos.objects.filter(
            Q(titulo__icontains=search) |
            Q(sub_titulo__icontains=search) |
            Q(area_acervo__icontains=search) |
            Q(assunto__icontains=search)
        ).order_by("id")[:3]

        revistas = Revistas.objects.filter(
            Q(titulo__icontains=search) |
            Q(sub_titulo__icontains=search) |
            Q(area_acervo__icontains=search) |
            Q(assunto__icontains=search)
        ).order_by("id")[:3]

        # Adiciona um atributo 'tipo' para cada item
        for l in livros:
            l.tipo = "Livro"
        for p in periodicos:
            p.tipo = "Periódico"
        for r in revistas:
            r.tipo = "Revista"

        # Combina e ordena por tipo
        items = list(livros) + list(periodicos) + list(revistas)
        tipo_ordem = {"Livro": 0, "Periódico": 1, "Revista": 2}
        items.sort(key=lambda x: tipo_ordem[x.tipo])

        return items
