from django.db import models

class ClAgenda(models.Model):
    AgeData = models.DateField('Data')
    AgeHora = models.TimeField('Hora')
    AgeInfo = models.CharField('indormação', max_length=100)
    AgePrio = models.CharField('Prioridade', max_length = 1, default='A',
                            choices=(('A','Alta'), ('M', 'Media'), ('B','Baixa')))
    AgeStat = models.CharField('Status', max_length=1, default= 'A',
                             choices=(('A','Aberto'), ('C','Concluido'), ('P', 'Pendente')))

def __str__(self):
    return f'{self.AgeData.strftime("%d/%m/%Y")} -'\
           f'{self.AgeHora.strftime("%H:%H")}'

class Meta: ordering = {'AgeData','AgeHora'}
# Create your models here.
