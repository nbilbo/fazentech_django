from django.urls import reverse
from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=60, blank=False, unique=True)
    descricao = models.TextField(max_length=100, blank=True)
    preco = models.FloatField(blank=False, default=0)
    disponibilidade = models.BooleanField(blank=False, default=True)
    slug = models.SlugField(max_length=60, blank=False, unique=True)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('produtos:detalhe_produto', kwargs={'slug':self.slug})        
    
