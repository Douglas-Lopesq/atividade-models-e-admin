from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Produto")
    codigo = models.CharField(max_length=100, unique=True, verbose_name="Código do Produto")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    quantidade = models.IntegerField(verbose_name="Quantidade em Estoque")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        ordering = ['-data_criacao']
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.nome} ({self.codigo})"

class Categoria(models.Model):



class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=255, verbose_name="Nome da empresa")
    endereco = models.
    CNPJ
    contato
    tipo_produto
