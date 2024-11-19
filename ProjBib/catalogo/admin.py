from django.contrib import admin
from catalogo.models import ClAutor, ClLivro, ClEditora, ClExemplar
# Definindo os campos para os autores
class ClAutorAdmin(admin.ModelAdmin):
    list_display = ('autor', 'dtnasc', 'dtmort')
    fields = ['autor', ('dtnasc', 'dtmort')]
admin.site.register(ClAutor, ClAutorAdmin)
# Define a listagem dos exemplares
class ClExemplarListagem(admin.TabularInline): model = ClExemplar; extra = 0
# Definindo os campos para os livros
class ClLivroAdmin(admin.ModelAdmin):
    list_display = ('titul', 'autor', 'edito', 'categ')
    inlines = [ClExemplarListagem]
    list_filter = ('categ', 'edito', 'autor')
    fields = ['titul', ('autor', 'edito'), 'categ', 'descr']
admin.site.register(ClLivro, ClLivroAdmin)# serve para registrar o admin
# Definindo os campos para as editoras
class ClEditoraAdmin(admin.ModelAdmin): pass
admin.site.register(ClEditora, ClEditoraAdmin)
# Definindo os campos para os exemplares
class ClExemplarAdmin(admin.ModelAdmin):
    list_display = ('registro', 'livro', 'retorno', 'status')
    list_filter = ('retorno', 'status')
    fieldsets = (('Dados do livro', {'fields': ('livro', 'registro', 'detalhes')}),
                 ('Disponibilidade', {'fields': ('retorno', 'status')}))
admin.site.register(ClExemplar, ClExemplarAdmin)
