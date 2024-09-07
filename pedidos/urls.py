from django.urls import path
from .views import lista_pedidos, detalhe_pedido, criar_pedido





urlpatterns = [
    path('criar/', criar_pedido, name='criar_pedido'),
    path('pedidos/', lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:id>/', detalhe_pedido, name='detalhe_pedido'),
]
