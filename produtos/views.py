from django.shortcuts import render
from django.views.generic import DetailView
from .models import Produto


def index(request):
    produtos = Produto.objects.all()
    content = {'produtos':produtos}
    
    return render(request, 'produtos/index.html', content)

class DetalheProduto(DetailView):
    model = Produto
    template_name = 'produtos/detalhe_produto.html'
    
