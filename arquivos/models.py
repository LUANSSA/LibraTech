from django.db import models

# Create your models here.
import os
from datetime import datetime
from django.db import models
from django.utils.text import slugify


def caminho_arquivo(instance, filename):
    """
    Define o caminho e o nome do arquivo salvo.
    Usa o título do arquivo (slugificado) + data/hora para garantir unicidade.
    """
    _, extensao = os.path.splitext(filename)
    titulo_slug = slugify(instance.titulo) if instance.titulo else "sem-titulo"
    data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    novo_nome = f"{titulo_slug}_{data}{extensao}"
    return os.path.join("arquivos/privados", novo_nome)


class Arquivos(models.Model):
    titulo = models.CharField("Título", max_length=300, null=False, blank=False)
    descricao = models.TextField("Descrição", null=True, blank=False)
    colecao = models.CharField("Coleção", max_length=300, null=True, blank=True)
    tipo_arquivo = models.CharField("Tipo de Arquivo", max_length=100, null=False, blank=False)  # PDF, DOCX, JPG, etc.
    arquivo = models.FileField("Arquivo", upload_to=caminho_arquivo)
    autor = models.CharField("Autor", max_length=200, null=True, blank=True)
    data_publicacao = models.DateField("Data de Publicação", null=True, blank=True)
    assunto = models.CharField("Assunto", max_length=300, null=True, blank=True)
    area_acervo = models.CharField("Área do Acervo", max_length=300, null=True, blank=True)
    chamada = models.CharField("Chamada", max_length=300, null=True, blank=True)
    num_tombamento = models.CharField("Nº de Tombamento", max_length=300, null=True, blank=True)
    referencia_ABNT = models.TextField("Referência ABNT", null=True, blank=True)
    nota = models.TextField("Nota", null=True, blank=True)
    disponibilidade = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"
        ordering = ["-data_cadastro"]

    def __str__(self):
        return self.titulo
