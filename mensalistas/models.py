from django.db import models


class Mensalista(models.Model):
    veiculo = models.ForeignKey('veiculos.Veiculo', on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)  
    