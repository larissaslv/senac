from django.db import models
import uuid
# Create your models here.
# classe para construir e acessar a tabela dos autores
class ClAutor(models.Model):
    # atributos da classe
    autor = models.CharField('Autor', max_length = 50, help_text = 'Nome do Autor')
    dtnasc = models.DateField('Nascimento', null = True, blank = True)
    dtmort = models.DateField('Morte', null = True, blank = True)
    # métodos da classe
    def __str__(self): return self.autor
    class Meta: ordering = ['autor']
# classe para construir e acessar a tabela das editoras
class ClEditora(models.Model):
    # atributos da classe
    editora = models.CharField(max_length = 50, help_text = 'Nome da Editora')
    # métodos da classe
    def __str__(self): return self.editora
    class Meta: ordering = ['editora']
# classe para construir e acessar a tabela dos livros
class ClLivro(models.Model):
    titul = models.CharField('Título', max_length = 50, help_text = 'Nome do livro')
    autor = models.ForeignKey(ClAutor, on_delete = models.SET_NULL, null = True, help_text = 'Autor do livro')
    edito = models.ForeignKey(ClEditora, on_delete = models.SET_NULL, null = True, help_text = 'Editora do Livro')
    descr = models.CharField('Descrição', max_length = 500, help_text = 'Descrição do livro')
    categ = models.CharField('Categoria', max_length = 1, help_text = 'Status do livro',
                             choices = (('F', 'Ficção'), ('R', 'Romance'), ('D', 'Drama'),
                                        ('A', 'Aventura'), ('T', 'Técnico'), ('I', 'Indefinido')),
                             blank = True, default = 'I')
    def __str__(self): return self.titul
    class Meta: ordering = ['titul']
# classe para construir e acessar a tabela dos exemplares
class ClExemplar(models.Model):
    registro = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Registro único para esse exemplar')
    livro = models.ForeignKey(ClLivro, on_delete = models.SET_NULL, null = True)
    detalhes = models.CharField(max_length = 50, help_text = 'Detalhes do exemplar')
    retorno = models.DateField(null = True, blank = True)
    status = models.CharField(max_length = 1, help_text = 'Status do exemplar',
                              choices = (('M', 'Manutenção'), ('D', 'Disponível'), ('R', 'Retirado')),
                              blank = True, default = 'M')
    def __str__(self): return f'{self.registro}({self.livro.titul})'
    class Meta: ordering = ['retorno']
