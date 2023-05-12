from django.contrib import admin

# Register your models here.
from .models import Product, Filament

admin.site.register(Product)
admin.site.register(Filament)