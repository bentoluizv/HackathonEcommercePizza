from django.urls import path
from .views import listar_pedidos, detalhes_pedido, criar_pedido





urlpatterns = [
    path('criar/', criar_pedido, name='criar_pedido'),
    path('pedidos/', listar_pedidos, name='lista_pedidos'),
    path('pedidos/<int:id>/', detalhes_pedido, name='detalhe_pedido'),
]
