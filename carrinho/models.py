from django.db import models
from produtos.models import ProdutoCatalogo
from django.contrib.auth.models import User


class Carrinho(models.Model):    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(ProdutoCatalogo, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def get_total(self):
        return self.quantidade * self.produto.preco  