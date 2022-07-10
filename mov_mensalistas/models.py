from django.db import models


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(
        'mensalistas.Mensalista',
        on_delete=models.CASCADE,
        related_name='mov_mensalista_mensalista',
        verbose_name='Mensalista'
    )
    pago_em = models.DateField(verbose_name='Pago em')
    valor_pago = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Valor pago'
    )

    def __str__(self):
        return str(self.mensalista) +' => '+ str(self.pago_em)
