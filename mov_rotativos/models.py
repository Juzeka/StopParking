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
    placa = models.CharField(
        max_length=8,
        blank=False,
        null=False,
        verbose_name='Placa do veículo'
    )
    valor_pago = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Valor pago'
    )
    pago = models.BooleanField(default=False)


    class Meta:
        ordering = ['-pk']
        verbose_name = 'Rotativo'
        verbose_name_plural = 'Rotativos'

    def __str__(self):
        return str(self.placa)