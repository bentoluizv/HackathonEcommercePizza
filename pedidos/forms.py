from django import forms
from .models import Pedido, ItemPedido



class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'status', 'total']   

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido', 'produto', 'quantidade', 'preco', 'variacao']   
