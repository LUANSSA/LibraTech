from django.db import models

# Create your models here.

class Periodicos(models.Model):
    titulo = models.CharField("Título", max_length=300)
    sub_titulo = models.CharField("Subtítulo", max_length=300, null=True, blank=True)
    issn = models.CharField("ISSN", max_length=20, unique=True)
    frequencia = models.CharField("Frequência", max_length=100, null=True, blank=True)
    periodo_inicio = models.DateField("Início de Publicação", null=True, blank=True)
    periodo_fim = models.DateField("Fim de Publicação", null=True, blank=True)
    volume = models.CharField("Volume", max_length=100, null=True, blank=True)
    numero = models.CharField("Número", max_length=100, null=True, blank=True)
    editora = models.CharField("Editora", max_length=200, null=True, blank=True)
    local = models.CharField("Local", max_length=200, null=True, blank=True)
    assunto = models.CharField("Assunto", max_length=300, null=True, blank=True)
    area_acervo = models.CharField("Área do Acervo", max_length=300, null=True, blank=True)
    referencia_ABNT = models.TextField("Referência ABNT", null=True, blank=True)
    nota = models.TextField("Nota", null=True, blank=True)
    disponibilidade = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
