from django.shortcuts import render
from .models import Contato


def home(request):
    data = 'active'
    return render(request, 'website/index.html',{'data':data})


def contato(request):
    data = 'active'
    mensagem = ''
    if request.method == 'POST':
        try:
            contato = {}
            contato['nome'] = request.POST.get('nome')
            contato['sobrenome'] = request.POST.get('sobrenome')
            contato['email'] = request.POST.get('email')
            contato['endereco'] = request.POST.get('endereco')
            contato['mensagem'] = request.POST.get('mensagem')
            #contato['receber_noticias'] = request.POST.get('receber_noticias')
            if request.POST.get('receber_noticias') == 'on':
                contato['receber_noticias'] = 'True'
            else: 
                contato['receber_noticias'] = 'False'
            
            Contato.objects.create(**contato)
        except Exception as e:
            mensagem = str(e)
        else:
            mensagem = 'Contato realizado com sucesso!'
    
    
    return render(request, 'website/contato.html',{'data':data,'msn':mensagem})


def servico(request):
    data = 'active'
    return render(request, 'website/servico.html',{'data':data})


def sobre(request):
    data = 'active'
    return render(request, 'website/sobre.html',{'data':data})


def planos(request):
    data = 'active'
    return render(request, 'website/planos.html',{'data':data})