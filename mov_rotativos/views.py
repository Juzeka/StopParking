from django.shortcuts import render, redirect
from .models import MovRotativo
from .forms import MovRotativoForm
from django.contrib.auth.decorators import login_required


@login_required()
def lista_mov_rotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {
        'mov_rotativos': mov_rotativos,
        'form': form
    }

    return render(request, 'core/lista_mov_rotativos.html', data)

@login_required()
def mov_rotativo_novo(request):
    form = MovRotativoForm(request.POST or None)

    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_rotativos')

@login_required()
def mov_rotativo_update(request, id):
    mov_rotativo = MovRotativo.objects.get(id = id)
    form = MovRotativoForm(request.POST or None, instance=mov_rotativo)
    data = {
        'mov_rotativo': mov_rotativo,
        'form': form
    }

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
        return render(
            request,
            'core/mov_rotativo_delete_confirm.html',
            {'mov_rotativo': mov_rotativo}
        )
