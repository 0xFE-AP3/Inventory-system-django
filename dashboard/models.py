from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('D900', 'D900'),
    ('CS2100', 'CS2100'),
    ('CS2200', 'CS2200'),
)

class Product(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=True)
    codice = models.CharField(max_length=100, blank=False, unique=True, null=True)
    quantita = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Prodotti'

    def __str__(self):
        return f'{self.nome}---{self.codice}---{self.quantita}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True, verbose_name="numero pezzi")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Scaricati'

