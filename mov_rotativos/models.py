from django.db import models
import math


class MovRotativo(models.Model):
    checkin = models.DateTimeField(
        auto_now=False,
        verbose_name='Checkin'
    )
    checkout = models.DateTimeField(
        auto_now=False,
        null=True,
        blank=True,
        verbose_name='Checkout'
    )
    valor_hora = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Valor por hora'
    )
    veiculo = models.ForeignKey(
        'veiculos.Veiculo',
        on_delete=models.CASCADE,
        related_name='mov_rotativo_veiculo',
        verbose_name='Valor por hora'
    )
    pago = models.BooleanField(default=False)

    def horas_total(self):
        try:
            return math.ceil(
                (self.checkout-self.checkin).total_seconds() / 3600
            )
        except:
            pass
    def total(self):
        try:
            return self.valor_hora * self.horas_total()
        except:
            pass

    def __str__(self):
        return str(self.veiculo)