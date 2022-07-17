from django.shortcuts import render, redirect
from .models import MovRotativo
from .forms import MovRotativoForm, MovRotativoChekinForm, MovRotativoChekoutForm
from django.contrib.auth.decorators import login_required
from utils.views import CreateView
from django.utils import timezone
from configuracoes.models import Configuracao
import math
from decimal import Decimal


CONFIG = Configuracao.objects.first()

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


class CheckinView(CreateView):
    template_name = 'core/index.html'
    model = MovRotativo
    form_class = MovRotativoChekinForm
    success_url = '/admin_system/'

    def form_valid(self, form):
        return super().form_valid(form)

@login_required()
def checkin(request):
    data = request.POST.copy()
    data['checkin'] = timezone.now()

    form = MovRotativoChekinForm(data or None)

    if form.is_valid():
        form.save()

    return redirect('core_home')

@login_required()
def checkout(request, id):
    rotativo = MovRotativo.objects.get(id=id)
    rotativo.checkout = timezone.now()
    rotativo.valor_pago = calcular_valor_apagar(request, None, rotativo)
    rotativo.pago = True
    rotativo.save()

    return redirect('core_home')

def calcular_valor_apagar(request, id, rotativo=None):
    if not rotativo:
        rotativo = MovRotativo.objects.get(id=id)

    agora = timezone.now()
    valor_hora = CONFIG.valor_hora
    result = (agora - rotativo.checkin).total_seconds() / 3600

    hora_minuto = f'{round(Decimal(result), 1)}'.split('.')
    hora = int(hora_minuto[0])
    minuto = int(hora_minuto[1])

    if minuto >= 5:
        minuto = 0.5
        valor_apagar = Decimal(hora + minuto) * valor_hora
    else:
        if (minuto > 0 and minuto < 5 and hora == 0) or (minuto == 0 and hora == 0):
            valor_apagar = valor_hora / 2
        else:
            minuto = 0
            valor_apagar = Decimal(hora + minuto) * valor_hora

    return valor_apagar