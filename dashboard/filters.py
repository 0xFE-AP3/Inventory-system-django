from dataclasses import field
import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ProductFilter(django_filters.FilterSet):

    nome = CharFilter(field_name='nome', lookup_expr='icontains')
    codice= CharFilter(field_name='codice', lookup_expr='icontains')
    
    class Meta:
        model = Product
        fields ='__all__'
        exclude = ['quantita']