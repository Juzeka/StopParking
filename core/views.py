from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa,Veiculo,MovRotativo,Mensalista,MovMensalista
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    return render(request, 'core/index.html')


@login_required()
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas':pessoas, 'form':form}
    return render(request, 'core/lista_pessoas.html', data)


@login_required()
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required()
def pessoa_update(request, id):
    data ={}
    pessoa = Pessoa.objects.get(id = id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa']= pessoa
    data['form']= form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request,'core/update_pessoas.html',data)


@login_required()
def pessoa_delete(request,id):
    pessoa = Pessoa.objects.get(id = id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/pessoa_delete_confirm.html',{'pessoa':pessoa})


@login_required()
def  lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos':veiculos, 'form':form}
    return render(request, 'core/lista_veiculos.html',data)


@login_required()
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required()
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id = id)
    form = VeiculoForm(request.POST or None, instance= veiculo)
    data ['veiculo'] = veiculo
    data ['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


@login_required()
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request,'core/veiculo_delete_confirm.html',{'veiculo':veiculo})


@login_required()
def lista_mov_rotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'mov_rotativos': mov_rotativos,'form':form}
    return render(request, 'core/lista_mov_rotativos.html',data)


@login_required()
def mov_rotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_rotativos')


@login_required()
def mov_rotativo_update(request, id):
    data = {}
    mov_rotativo = MovRotativo.objects.get(id = id)
    form = MovRotativoForm(request.POST or None, instance= mov_rotativo)
    data ['mov_rotativo'] = mov_rotativo
    data ['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_rotativos')
    else:
        return render(request, 'core/update_mov_rotativo.html', data)


@login_required()
def mov_rotativo_delete(request, id):
    mov_rotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        mov_rotativo.delete()
        return redirect('core_lista_mov_rotativos')
    else:
        return render(request,'core/mov_rotativo_delete_confirm.html',{'mov_rotativo':mov_rotativo})


@login_required()
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas':mensalistas,'form': form}
    return render(request, 'core/lista_mensalistas.html',data)


@login_required()
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


@login_required()
def lista_mov_mensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mensalistas':mov_mensalistas, 'form': form}
    return render(request,'core/lista_mov_mensalistas.html',data)


@login_required()
def mensalista_updade(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id = id)
    form = MensalistaForm(request.POST or None, instance= mensalista)
    data ['mensalista'] = mensalista
    data ['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)


@login_required()
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request,'core/mensalista_delete_confirm.html',{'mensalista':mensalista})


@login_required()
def mov_mensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_mensalistas')


@login_required()
def mov_mensalista_update(request, id):
    data = {}
    mov_mensalista = MovMensalista.objects.get(id = id)
    form = MovMensalistaForm(request.POST or None, instance= mov_mensalista)
    data ['mov_mensalista'] = mov_mensalista
    data ['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_mensalistas')
    else:
        return render(request, 'core/update_mov_mensalista.html', data)


@login_required()
def mov_mensalista_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov_mensalista.delete()
        return redirect('core_lista_mov_mensalistas')
    else:
        return render(request,'core/mov_mensalista_delete_confirm.html',{'mov_mensalista':mov_mensalista})



