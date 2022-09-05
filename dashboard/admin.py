from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group 
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = 'Arredo System Inventario Sezione Admin'

class ProductAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'codice', 'quantita')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.unregister(Group)