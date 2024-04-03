from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import imovel
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'base.html')

def pesquisa(request):
    if request.method == 'POST':
        pesquisa_atual = request.POST['pesquisa_atual']

        
    
        imoveis = imovel.objects.filter( Q(id__contains=pesquisa_atual) |
                                         Q(num_contrib__contains=pesquisa_atual) |
                                         Q(nome_logradoro_imovel__contains = pesquisa_atual)  |
                                         Q(num_imovel__contains=pesquisa_atual) |
                                         Q(complemento_imovel__contains=pesquisa_atual) |
                                         Q(bairro_imovel__contains=pesquisa_atual) |
                                         Q(cep_imovel__contains=pesquisa_atual) |
                                         Q(area_tereno__contains=pesquisa_atual) |
                                         Q(metro_quad_terreno__contains=pesquisa_atual) 
                                         )



        
        return render(request, 'pesquisa.html', {"pesquisa_atual":pesquisa_atual, 'imoveis': imoveis})
        
    else:
        return render(request, 'pesquisa.html', {})
