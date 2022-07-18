from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm
from mov_rotativos.models import MovRotativo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    date_now = timezone.now()
    rotativos = MovRotativo.objects.filter(checkin__icontains=date_now.date())

    data = {
        'rotativos': rotativos,
        'hoje': date_now
    }

    return render(request, 'core/index.html', data)

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
    pessoa = Pessoa.objects.get(id = id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data = {
        'pessoa': pessoa,
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request,'core/update_pessoas.html', data)

@login_required()
def pessoa_delete(request,id):
    pessoa = Pessoa.objects.get(id = id)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(
            request,
            'core/pessoa_delete_confirm.html',
            {'pessoa': pessoa}
        )