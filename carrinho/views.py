from django.shortcuts import render, redirect, get_list_or_404
from produtos.models import ProdutoCatalogo
from .models import Carrinho, ItemCarrinho


 
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(ProdutoCatalogo, id=produto_id)
    carrinho = Carrinho.objects.get(usuario=request.user)  

    # Verificar se o produto já está no carrinho
    item_carrinho, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)

    if not created:
        item_carrinho.quantidade += 1  # Aumenta a quantidade se já estiver no carrinho
    item_carrinho.save()

    return redirect('visualizar_carrinho.html')

def visualizar_carrinho(request):
    carrinho = Carrinho.objects.get(usuario=request.user)  # Carrinho do usuário logado
    itens = carrinho.itens.all()  # Pega todos os itens do carrinho
    total_carrinho = sum(item.produto.preco * item.quantidade for item in itens) #calcula total carrinho
    
    return render(request, 'visualizar_carrinho.html', {'carrinho': carrinho, 'itens': itens, 'total_carrinho': total_carrinho,})


def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    item.delete()

    return redirect('visualizar_carrinho.html')


def atualizar_carrinho(request, item_id):
    item = get_list_or_404(ItemCarrinho, id=item_id)
    
    if request.method == 'POST':
        quantidade = request.POST.get('quantidade')
        if quantidade.isdigit() and int(quantidade) > 0:
            item.quantidade = int(quantidade)
            item.save()
        else:
            item.delete()  #remove ítem se quant.for inválida
    return redirect('visualizar_carrinho') 