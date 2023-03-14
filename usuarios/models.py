from django.db import models
from django.contrib.auth.models import AbstractUser

class Cidadao(AbstractUser):
    id = models.AutoField(primary_key=True, null=False)
    cpf_cnpj = models.CharField(max_length=14)
    cep = models.CharField(max_length=8, blank=True)
    cidade = models.CharField(max_length=20, blank=True)
    rua = models.CharField(max_length=30, blank=True)
    bairro = models.CharField(max_length=30, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=80, null=True, blank=True)