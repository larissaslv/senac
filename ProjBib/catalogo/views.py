from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalogo.models import ClAutor, ClEditora, ClLivro, ClExemplar

def index(request):#
    template= loader.get_template('index.html')# loader é o carregar, vai pegar o template com esse nome.
    num_livros = ClLivro.objects.all().count()#vou pegar todos os objetos que pertencem a classe livros. o objeto é o livro em si. Esses objetos serão contados.
    num_exemplares = ClExemplar.objects.all().count()# Pegar todos os objetos da classe exemplares e contá-los.
    num_disponiveis= ClExemplar.objects.filter(status='D').count()# Pegar os objts da classe exemplar e filtrá-los com o status d
    num_autores = ClAutor.objects.all().count()
    num_editoras = ClEditora.objects.all().count()# num_editoras recebe todos os objs da classe ClEditoras e vai conta-los.
    num_visitas= request.session.get('num_visitas', 1)
    request.session['num_visitas'] = num_visitas +1
    context = {'url_pagina':request.get_full_path(),
               'num_livros':num_livros,
               'num_exemplares': num_exemplares,
               'num_disponiveis':num_disponiveis,
               'num_autores':num_autores,
               'num_editoras': num_editoras,
               'num_visitas':num_visitas}
    return HttpResponse(template.render(context,request))

def livros(request):
    template = loader.get_template('livros.html')
    list_livros = ClLivro.objects.all()
    num_visitas_livros=request.session.get('num_visitas_livros',0)
    request.session['num_visitas_livros']=num_visitas_livros+1
    context = {'url_pagina':request.get_full_path(),
               'list_livros': list_livros,
               'num_visitas_livros':num_visitas_livros}
    return HttpResponse(template.render(context,request))

def consiste_categ(categ):
    if categ == 'F': nome_categ = 'Ficcao'
    if categ == 'R': nome_categ = 'Romance'
    if categ == 'D': nome_categ = 'Drama'
    if categ == 'T': nome_categ = 'Tecnico'
    if categ == 'I': nome_categ = 'Indefinido'
    return nome_categ #Acho que vai dar erro

def livro_det(request, chave_pk):
    template = loader.get_template('livro_det.html')
    livro=ClLivro.objects.get(pk=chave_pk)
    context = { 'url_pagina': request.get_full_path(),
                'titul': livro.titul,
                'autor': livro.autor,
                'edito':livro.edito,
                'descr':livro.descr,
                'categ': consiste_categ(livro.categ)}
    return HttpResponse(template.render(context,request))

def autor_det(request, chave_pk):
    template = loader.get_template('autor_det.html')
    livro = ClLivro.objects.get(pk=chave_pk)
    context = {'url_pagina':request.get_full_path(),
               'autor': livro.autor,
               'nascimento': livro.autor.dtnasc,
               'falecimento': livro.autor.dtmort}
    return HttpResponse(template.render(context, request))

def edito_det(request, chave_pk):
    template = loader.get_template('edito_det.html')
    livro = ClLivro.objects.get(pk=chave_pk)
    # url_pagina recebe a url desta página
    context = {'url_pagina':request.get_full_path(),
               'editora': livro.edito,
               'dt_fund': livro.edito.dt_fund,
               'endereco': livro.edito.endereco}
    return HttpResponse(template.render(context, request))

def exemplares (request, chave_pk):
    template = loader.get_template('exemplares.html')
     # url_pagina recebe a url desta página
    url_pagina = request.get_full_path()
    # se chave_pk = t retorna todos os exemplares
    if chave_pk == 't':
         # todos os exemplares cadastrados
         list_exemplares = ClExemplar.objects.all()
         pagina_msg = 'Todos os exemplares cadastrados'
    else:
# se chave_pk = d retorna os exemplares disponiveis
    if chave_pk == 'd':
            # list_exemplares recebe os livros com status = d
            list_exemplares = ClExemplar.objects.filter(status='d')
            pagina_msg = 'Exemplares cadastrados disponíveis'
    else:
 # se chave_pk for uma pk numerica do livro selecionado...
# ...retorna os exemplares do livro selecionado
# int(chave_pk): converte chave_pk para inteiro


    reglivro = ClLivro.objects.get(pk=chave_pk)
    list_exemplares = ClExemplar.objects.filter(livro=reglivro)
    pagina_msg = 'Exemplares do livro selecionado'

    context = {'url_pagina': url_pagina,
               'url_pagina_ant': url_pagina[:-(len(chave_pk)+11)] ,
               'list_exemplares': list_exemplares,
               'pagina_msg': pagina_msg}
    return HttpResponse(template.render(context,request))
# exemplar_det: apresenta os detalhes do exemplar selecionado
# chave_pk: chave padrão uuid (string)
def exemplar_det(request, chave_pk):
    template = loader.get_template('exemplar_det.html')
    context = {'exemplar': ClExemplar.objects.get(pk=chave_pk)}
    return HttpResponse(template.render(context, request))


