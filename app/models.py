from django.db import models

# Create your models here.
class FormCliente(models.Model):
    
    nome = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    pizzarias = models.CharField(max_length=100)


class Massa(models.Model):
    massa_opcoes = [
    ('np', 'napolitana'),
    ('ni', 'nova-iorquina'),
    ('sn', 'siciliana'),
    ('vt', 'vegetariana'),
    ('vg', 'vegana'),
    ('in', 'integral'),

    ]

    molho_opcoes = [
    ('tr', 'tradicional'),
    ('gz', 'gorgonzola'),
    ('ps', 'parisiense'),
    ('pc', 'picante'),
    ('sj', 'soja'),

    ]

    ingredientes_veg = [
    ('tf', 'tofu'),
    ('mc', 'muçarela de castanha'),
    ('cj', 'carne de jaca'),
    ('pa', 'parmesão de amendoim'),
    ('ev', 'ervilha'),
    ('ap', 'alho-poró'),
    ('cf', 'couve-flor'),
    ('rc', 'rúcula'),
    ('ch', 'champignon'),
    ('tm', 'tomate'),
    ('tc', 'tomate cereja'),
    ('ab', 'abobrinha'),
    ('mj', 'manjerião'),
    ('pv', 'presunto vegetal'),
    ('az', 'azeitona'),
    ('ap', 'azeitona preta'),
    ('or', 'oregano'),

    ]

    ingredientes_integral = [
    ('mc', 'muçarela'),
    ('pa', 'parmesão'),
    ('fg', 'frango'),
    ('at', 'atum'),
    ('br', 'brócolis'),
    ('gz', 'gorgonzola'),
    ('ov', 'ovo'),
    ('tm', 'tomate'),
    ('tc', 'tomate cereja'),
    ('pl', 'palmito'),
    ('az', 'azeitona'),
    ('ap', 'azeitona preta'),
    ('cb', 'cebola'),
    ('ml', 'milho'),

    ]

    ingredientes_opcoes = [
    ('mc', 'muçarela'),
    ('pa', 'parmesão'),
    ('tm', 'tomate'),
    ('tc', 'tomate cereja'),
    ('mj', 'manjerião'),
    ('az', 'azeitona'),
    ('ap', 'azeitona preta'),
    ('or', 'oregano'),
    ('bc', 'bacon'),
    ('ps', 'presunto'),
    ('pr', 'peru'),
    ('fg', 'frango'),
    ('ov', 'ovo'),
    ('mc', 'milho'),
    ('cy', 'catupiry'),
    ('ch', 'cheddar'),

    ]

    ingredientes_doce = [
    ('ma', 'maçã'),
    ('bn', 'banana'),
    ('nt', 'nutella'),
    ('ch', 'chocolate'),
    ('cb', 'chocolate branco'),
    ('mg', 'morango'),
    ('dl', 'doce de leite'),
    ('br', 'brigadeiro'),
    ('pt', 'prestigio'),
    ('ln', 'leite ninho'),
    ('so', 'sorvete'),
    ('ab', 'abacaxi'),
    ('rj', 'romeu e julieta'),
    ('om', 'ovomaltine'),
    ('pc', 'paçoca'),
    ]

    massa = models.CharField(max_length=60, choices=massa_opcoes, default="")
    molho = models.CharField(max_length=60, choices=molho_opcoes, default="")
    ingredientes_veg = models.CharField(max_length=60, default="")
    ingredientes_integral = models.CharField(max_length=60, default="")
    ingredientes_opcoes = models.CharField(max_length=60, default="")
    ingredientes_doce = models.CharField(max_length=60, default="")