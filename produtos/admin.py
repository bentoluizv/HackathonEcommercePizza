from django.contrib import admin
from produtos.models import Bebida, Pizza, Pedido, ProdutoCatalogo, Variacao, ItemPedidoModel
 


 
admin.site.register(Pizza)
admin.site.register(Bebida)


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedidoModel
    extra = 1
    
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'status', 'total', 'data_criacao']
    inlines = [ItemPedidoInline]