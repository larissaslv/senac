from django.db import models

class ClEsporte(models.Model):
    EspNome=models.CharField('Nome do Esporte',
                             max_length=20,
                             )

    def __str__(self):
        return self.EspNome
    class Meta:
        ordering=['EspNome']

class ClMusica(models.Model):
    MusNome=models.CharField('Nome da Musica',
                             max_length=20,
                             )

    def __str__(self):
        return self.MusNome
    class Meta:
        ordering=['MusNome']

class ClFesta(models.Model):
    FestNome=models.CharField('Festa',
                              max_length=20,
                              )

    def __str__(self):
        return self.FestNome
    class Meta:
        ordering=['FestNome']

class ClEstudo(models.Model):
    EstNome=models.CharField('Estudos',
                             max_length=20,
                             )

    def __str__(self):
        return self.EstNome
    class Meta:
        ordering=['EstNome']

class ClCultura(models.Model):
    CultNome=models.CharField('Cultura',
                              max_length=20,
                              help_text='Nome Cultura')

    def __str__(self):
        return self.CultNome
    class Meta:
        ordering=['CultNome']

class ClCandidato(models.Model):
    cannome=models.CharField('Nome do candidato',
                             max_length=50,
                             )
    EspNome=models.ForeignKey(ClEsporte,
                              on_delete=models.SET_NULL,
                              null=True,
                              )
    MusNome=models.ForeignKey(ClMusica,
                              on_delete=models.SET_NULL,
                              null=True,
                              )
    FestNome=models.ForeignKey(ClFesta,
                               on_delete=models.SET_NULL,
                               null=True,
                               )
    EstNome=models.ForeignKey(ClEstudo,
                              on_delete=models.SET_NULL,
                              null=True,
                              )
    CultNome=models.ForeignKey(ClCultura,
                               on_delete=models.SET_NULL,
                               null=True,
                               )

    def __str__(self):
        return self.cannome
    class Meta:
        ordering=['cannome']

# Create your models here.
