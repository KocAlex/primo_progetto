from django.contrib import admin
from products.models import Product, Manufacturer


admin.site.register(Product)
admin.site.register(Manufacturer)