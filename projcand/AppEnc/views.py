from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppEnc.models import ClEstudo, ClCandidato,ClFesta,ClCultura,ClMusica,ClEsporte

def index (request):
    template = loader.get_template('index.html')
    list_Candidatos=ClCandidato.objects.all()
    nome_tit='Todos os candidatos'
    context={'list_Candidatos':list_Candidatos,
             'nome_tit':nome_tit}
    return HttpResponse(template.render(context,request))

def sel_esporte(request, tipo):
    template=loader.get_template('candidatos.html')
    list_candidatos=ClCandidato.objects.all()
    list_cand_selecionado=[]
    for candidato in list_candidatos:
        if str(candidato.EspNome) == tipo: list_cand_selecionado.append(candidato)
    nome_tit='Candidatos que gostam do esporte: '+tipo
    context={'list_cand_selecionado':list_cand_selecionado, 'prefixo':'esp',
             'nome_tit':nome_tit, 'tipo':tipo, 'voltar':request.META.get('HTTP_REFERER')}
    return HttpResponse(template.render(context,request))

def sel_musica(request, tipo):
    template = loader.get_template('candidatos.html')
    list_candidatos = ClCandidato.objects.all()
    list_cand_selecionado = []
    for candidato in list_candidatos:
        if str(candidato.MusNome) == tipo: list_cand_selecionado.append(candidato)
    nome_tit = 'Candidatos que gostam de música do tipo: ' + tipo
    context = {'list_cand_selecionado': list_cand_selecionado, 'prefixo':'mus',
               'nome_tit': nome_tit, 'tipo': tipo, 'voltar':request.META.get('HTTP_REFERER')}
    return HttpResponse(template.render(context, request))

def sel_festa(request, tipo):
    template = loader.get_template('candidatos.html')
    list_candidatos = ClCandidato.objects.all()
    list_cand_selecionado = []
    for candidato in list_candidatos:
        if str(candidato.FestNome) == tipo: list_cand_selecionado.append(candidato)
    nome_tit = 'Candidatos com o tipo de festa: ' + tipo
    context = {'list_cand_selecionado': list_cand_selecionado, 'prefixo':'fest',
               'nome_tit': nome_tit, 'tipo': tipo, 'voltar':request.META.get('HTTP_REFERER')}
    return HttpResponse(template.render(context, request))

def sel_estudo(request, tipo):
    template = loader.get_template('candidatos.html')
    list_candidatos = ClCandidato.objects.all()
    list_cand_selecionado = []
    for candidato in list_candidatos:
        if str(candidato.EstNome) == tipo: list_cand_selecionado.append(candidato)
    nome_tit = 'Candidatos que estudam: ' + tipo
    context = {'list_cand_selecionado': list_cand_selecionado, 'prefixo':'est',
               'nome_tit': nome_tit, 'tipo': tipo, 'voltar':request.META.get('HTTP_REFERER')}
    return HttpResponse(template.render(context, request))

def sel_cultura(request, tipo):
    template = loader.get_template('candidatos.html')
    list_candidatos = ClCandidato.objects.all()
    list_cand_selecionado = []
    for candidato in list_candidatos:
        if str(candidato.CultNome) == tipo: list_cand_selecionado.append(candidato)
    nome_tit = 'Candidatos com a preferência na cultura: ' + tipo
    context = {'list_cand_selecionado': list_cand_selecionado, 'prefixo':'cult',
               'nome_tit': nome_tit, 'tipo': tipo, 'voltar':request.META.get('HTTP_REFERER')}
    return HttpResponse(template.render(context, request))
'''
def comp_esp (request, tipo):
    template=loader.get_template('candidatos.html')
    list_candidatos=ClCandidato.objects.all()
    nome_tit='Candidatos com esportes iguais' + tipo
    context={'list_candidatos':list_candidatos,'nome_tit': nome_tit,
             'tipo_arg':'esp'}
    return HttpResponse(template.render(context,request))

def  comp_cult(request,tipo):
    template=loader.get_template('cultura.html')
'''
# Create your views here.
