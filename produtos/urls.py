from django.urls import path
from .views import listar_produtos, render_index
from . import views






urlpatterns = [
    path('', render_index, name='render_index'),
    path('', views.render_index, name='render_index'),
    path('produtos/', listar_produtos, name='listar_produtos'),

]
