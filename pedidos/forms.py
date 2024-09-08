from django import forms
from .models import Pedido, ItemPedidoModel  



class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'status', 'total']   

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedidoModel
        fields = ['produto', 'quantidade', 'preco', 'variacao']   
