from django.urls import path
from .views import index, DetalheProduto


app_name = 'produtos'

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', DetalheProduto.as_view(), name='detalhe_produto'),
]
