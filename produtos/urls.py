from django.urls import path
from .views import index, adicionar, atualizar, DetalheProduto


app_name = 'produtos'

urlpatterns = [
    # ex: /produtos/
    path('', index, name='index'),
    
    # ex: /produtos/adicionar/
    path('adicionar/', adicionar, name='adicionar'),
    
    path('atualizar/<slug:produto_slug>/', atualizar, name='atualizar'),
    
    # ex: /produtos/queijo/
    path('<slug:slug>/', DetalheProduto.as_view(), name='detalhe_produto'),
]
