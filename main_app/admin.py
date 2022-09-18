from django.contrib import admin

from main_app.models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
