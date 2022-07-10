from django.db import models
import math


class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null = True, blank = True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey('veiculos.Veiculo', on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        try:
            return math.ceil((self.checkout-self.checkin).total_seconds()/3600)
        except:
            pass
    def total(self):
        try:
            return self.valor_hora * self.horas_total()
        except:
            pass

    def __str__(self):
        return str(self.veiculo)