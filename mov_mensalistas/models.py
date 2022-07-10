from django.db import models


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(
        'mensalistas.Mensalista', on_delete=models.CASCADE
    )
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return str(self.mensalista) +' => '+ str(self.dt_pgto)
