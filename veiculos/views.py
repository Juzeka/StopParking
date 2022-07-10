from django.shortcuts import render, redirect
from .models import Veiculo
from .forms import VeiculoForm
from django.contrib.auth.decorators import login_required


@login_required()
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {
        'veiculos': veiculos,
        'form': form
    }
    return render(request, 'core/lista_veiculos.html',data)

@login_required()
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)

    if form.is_valid():
        form.save()

    return redirect('core_lista_veiculos')

@login_required()
def veiculo_update(request, id):
    veiculo = Veiculo.objects.get(id = id)
    form = VeiculoForm(request.POST or None, instance= veiculo)
    data = {
        'veiculo': veiculo,
        'form': form
    }

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
        return render(
            request,
            'core/veiculo_delete_confirm.html',
            {'veiculo': veiculo}
        )