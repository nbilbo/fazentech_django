from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Produto
from .forms import FormProduto


def index(request):
    produtos = Produto.objects.all()
    content = {'produtos':produtos}
    
    return render(request, 'produtos/index.html', content)

def adicionar(request):
    if request.method == 'POST':
        form = FormProduto(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/produtos/')
    else:
        context = {'form':FormProduto()}
        
        return render(request, 'produtos/adicionar.html', context)

def atualizar(request, produto_slug):
    produto = get_object_or_404(Produto, slug=produto_slug)
    
    if request.method == 'POST':
        form = FormProduto(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/produtos/')

    else:
        form = FormProduto(instance=produto)
        context = {'form':form}
    
        return render(request, 'produtos/atualizar.html', context)
    

class DetalheProduto(DetailView):
    model = Produto
    template_name = 'produtos/detalhe_produto.html'
    
