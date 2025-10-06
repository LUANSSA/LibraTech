from django.db import models

# Create your models here.


class Livros(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=300, null=False, blank=False)
    sub_titulo = models.CharField(verbose_name="Subtítulo", max_length=300, null=False, blank=False)
    colecao = models.CharField(verbose_name="Coleção", max_length=300, null=False, blank=False)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=False)
    edicao = models.CharField(verbose_name="Edição", max_length=300, null=False, blank=False)
    local = models.CharField(verbose_name="Local", max_length=300, null=False, blank=False)
    editora = models.CharField(verbose_name="Editora", max_length=300, null=False, blank=False)
    ano = models.IntegerField(verbose_name="Ano", null=False, blank=False)
    mes_ano_publicacao = models.DateField(verbose_name="Data de Publicação", null=False, blank=False)
    paginas = models.IntegerField(verbose_name="Páginas", null=False, blank=False)
    volume = models.CharField(verbose_name="Volume", max_length=300, null=False, blank=False)
    tomo = models.CharField(verbose_name="Tomo", max_length=300, null=False, blank=False)
    chamada = models.CharField(verbose_name="Chamada", max_length=300, null=False, blank=False)
    num_tombamento = models.CharField(verbose_name="Nº de Tombamento", max_length=300, null=False, blank=False)
    assunto = models.CharField(verbose_name="Assunto", max_length=300, null=False, blank=False)
    area_acervo = models.CharField(verbose_name="Área do Acervo", max_length=300, null=False, blank=False)
    referencia_ABNT = models.TextField(verbose_name="Referência ABNT", null=True, blank=True)
    nota = models.TextField(verbose_name="Nota", null=True, blank=True)
    disponibilidade = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
