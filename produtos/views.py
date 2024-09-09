from django.shortcuts import render
from .models import Bebida, Pizza, ProdutoCatalogo



def listar_produtos(request):
    produtos = ProdutoCatalogo.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def render_index(request):
    pizzas = Pizza.objects.all()
    bebidas = Bebida.objects.all()

    return render(request, 'index/home.html', {'pizzas': pizzas, 'bebidas': bebidas})
