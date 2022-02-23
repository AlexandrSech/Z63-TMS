from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name", "current_amont", "supplier", "update_date"]
    list_editable = ["current_amont"]