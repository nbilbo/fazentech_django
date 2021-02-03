from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Produto
from .forms import FormProduto


def index(request):
    context = {}
    url_parameter = request.GET.get('p')

    if url_parameter:
        produtos = Produto.objects.filter(nome__icontains=url_parameter)
    else:
        produtos = Produto.objects.all()
    
    if request.is_ajax():
        html = render_to_string(
            template_name='produtos/resultado_produtos.html',
            context={'produtos':produtos}
        )

        return JsonResponse(data={'resultado_produtos':html}, safe=False)

    context['produtos'] = produtos

    return render(request, 'produtos/index.html', context)

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
    
