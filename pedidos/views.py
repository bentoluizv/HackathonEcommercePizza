from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, ItemPedidoModel
from .forms import PedidoForm, ItemPedidoForm   

def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

def criar_pedido(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        item_form = ItemPedidoForm(request.POST)

        if pedido_form.is_valid() and item_form.is_valid():
            pedido = pedido_form.save() #Sava pedido
            item = item_form.save(commit=False) #Não salva ainda
            item.pedido = pedido #Atribuir pedido ao ítem
            item.save()  #Agora salva 
            return redirect('lista_pedidos')   
    else:
        pedido_form = PedidoForm()
        item_form = ItemPedidoForm()

    return render(request, 'criar_pedido.html', {
        'pedido_form': pedido_form,
        'item_form': item_form,
    })


def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'editar_pedido.html', {'form': form, 'pedido': pedido})

def detalhes_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'detalhe_pedido.html', {'pedido': pedido})

def deletar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'deletar_pedido.html', {'pedido': pedido})








 