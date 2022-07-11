from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MovMensalista
from .forms import MovMensalistaForm


@login_required()
def lista_mov_mensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {
        'mov_mensalistas': mov_mensalistas,
        'form': form
    }

    return render(request,'core/lista_mov_mensalistas.html', data)

@login_required()
def mov_mensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)

    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_mensalistas')

@login_required()
def mov_mensalista_update(request, id):
    mov_mensalista = MovMensalista.objects.get(id = id)
    form = MovMensalistaForm(request.POST or None, instance= mov_mensalista)
    data = {
        'mov_mensalista': mov_mensalista,
        'form': form
    }

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
        return render(
            request,
            'core/mov_mensalista_delete_confirm.html',
            {'mov_mensalista': mov_mensalista}
        )