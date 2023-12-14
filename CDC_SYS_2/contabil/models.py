from django.db import models
from datetime import datetime

class CalculoRecisorio(models.Model):
    # Colaborador
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=20)
    data_de_nascimento = models.DateField()
    admissao = models.DateField()
    demissao = models.DateField()


    # Dados Financeiros
    salario_bruto = models.DecimalField(max_digits=10, decimal_places=2)
    salario_liquido = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Dados Recisorios
    rescisao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    aviso_previo_proporcional = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    decimo_terceiro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ferias = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ferias_vencidas = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    indenizacao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fgts = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dias_trabalhados_no_ano = models.IntegerField()
    meses_trabalhados = models.IntegerField()
    aviso_previo_indenizado = models.BooleanField(default=False)
    motivo_rescisao = models.CharField(max_length=200, null=True, blank=True)


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    data_fim = models.DateField()


class Provisao(models.Model):
    projeto = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    rubrica = models.CharField(max_length=100, blank=True)
    categoria = models.CharField(max_length=100, blank=True)
    subcategoria = models.CharField(max_length=100, blank=True)
    detalhamento = models.TextField(blank=True)

    def _str_(self):
        return self.projeto
    


class Trabalhador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=20)
    data_de_nascimento = models.DateField()
    tipo_logradouro = models.CharField(max_length=50)
    nome_logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    projetos = models.ManyToManyField(Provisao, blank=True)

    def _str_(self):
        return f"{self.nome} ({self.cpf})"
