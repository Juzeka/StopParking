from django.shortcuts import render, redirect
from .models import Mensalista
from .forms import MensalistaForm
from django.contrib.auth.decorators import login_required


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
def mensalista_updade(request, id):
    mensalista = Mensalista.objects.get(id = id)
    form = MensalistaForm(request.POST or None, instance= mensalista)
    data = {
        'mensalista': mensalista,
        'form': form,
    }

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
        return render(
            request,
            'core/mensalista_delete_confirm.html',
            {'mensalista': mensalista}
        )
