from django.db import models

class Vendor(models.Model):
    cnpj = models.CharField(max_length=14)
    razaosocial = models.CharField(max_length=255)
    inscEstadual = models.CharField(max_length=12)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

