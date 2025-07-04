from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    
class Medico(models.model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=6, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, related_name='medicos')

    def __str__(self):
        return self.nome