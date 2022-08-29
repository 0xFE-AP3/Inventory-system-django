from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group 

admin.site.site_header = 'Arredo System Inventario Sezione Admin'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'category', 'codice', 'quantita')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.unregister(Group)