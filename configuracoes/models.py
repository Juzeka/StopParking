from django.db import models


class Configuracao(models.Model):
    valor_hora = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Valor por hora'
    )
    valor_mes = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Valor por mês'
    )

    def __str__(self):
        return 'Configuração'
