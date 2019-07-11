from django.db import models

# Create your models here.
class Pedido(models.Model):
    
    nome = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    pizzarias = models.CharField(max_length=100)

    def __str__(self):
        return self.nome