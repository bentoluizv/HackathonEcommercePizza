from django.contrib import admin
from django.urls import path, include 
from django.shortcuts import redirect



def home(request):
    return redirect('produtos:render_index')


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('carrinho/', include('carrinho.urls'))
]
