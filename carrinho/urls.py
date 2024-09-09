from django.urls import path
from .views import adicionar_ao_carrinho, visualizar_carrinho, remover_do_carrinho, atualizar_carrinho





urlpatterns = [
    path('adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_carrinho'),
    path('visualizar/', visualizar_carrinho, name='visualizar_carrinho'),
    path('remover/<int:item_id>/', remover_do_carrinho, name='remover_carrinho'),
    path('atualizar/<int:item_id>/', atualizar_carrinho, name='atualizar_carrinho'),
]

