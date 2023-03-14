from django.db import models
from usuarios.models import Cidadao

class Comentario(models.Model):
    descricao = models.TextField()
    resumo = models.CharField(max_length=50)
    topico = models.IntegerField()
    cep = models.CharField(max_length=8, blank=True)
    cidade = models.CharField(max_length=20, blank=True)
    rua = models.CharField(max_length=30, blank=True)
    bairro = models.CharField(max_length=30, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=80, null=True, blank=True)
    cidadao = models.ForeignKey(Cidadao, null=True, blank=True, on_delete=models.SET_NULL, related_name='comentarios')
    comentario_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respostas')