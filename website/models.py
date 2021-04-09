from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    mensagem = models.TextField()
    receber_noticias = models.BooleanField()

    def __str__(self):
        return self.nome
    