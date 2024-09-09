from django.contrib import admin
from .models import Pedido, ItemPedidoModel

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedidoModel
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'status', 'total', 'data_criacao']
    inlines = [ItemPedidoInline]

 
 