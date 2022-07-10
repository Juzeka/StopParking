from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.ForeignKey(
        Marca,
        on_delete=models.PROTECT,
        related_name='veiculo_marca',
        verbose_name='Marca'
    )
    placa = models.CharField(
        max_length=8,
        verbose_name='Placa'
    )
    propietario = models.ForeignKey(
        'core.Pessoa',
        on_delete=models.CASCADE,
        related_name='veiculo_pessoa',
        verbose_name='Propietario'
    )
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()

    def __str__(self):
        return self.placa