from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppAgenda.models import ClAgenda

def index(request):
    template = loader.get_template('index.html')
    num_comp = ClAgenda.objects.all().count()
    num_alta = ClAgenda.objects.filter(AgePrio='A').count()
    num_medi = ClAgenda.objects.filter(AgePrio='M').count()
    num_baix = ClAgenda.objects.filter(AgePrio='B').count()
    num_aber = ClAgenda.objects.filter(AgePrio='A').count()
    num_conc = ClAgenda.objects.filter(AgePrio='C').count()
    num_pend = ClAgenda.objects.filter(AgePrio='P').count()
    context = {'num_comp': num_comp,
               'num_alta': num_alta, 'num_medi': num_medi, 'num_baix': num_baix,
               'num_aber': num_aber, 'num_conc': num_conc, 'num_pend': num_pend}
    return HttpResponse(template.render(context,request))

def compromissos(request, AgeFiltro):
    template = loader.get_template('compromissos.html')
    list_comp = []
    if AgeFiltro == 'TC': list_comp = ClAgenda.objects.all().count()
    if AgeFiltro == 'PA': list_comp = ClAgenda.objects.filter(AgePrio='A')
    if AgeFiltro == 'PM': list_comp = ClAgenda.objects.filter(AgePrio='M')
    if AgeFiltro == 'PB': list_comp = ClAgenda.objects.filter(AgePrio='B')
    if AgeFiltro == 'SA': list_comp = ClAgenda.objects.filter(AgePrio='A')
    if AgeFiltro == 'SC': list_comp = ClAgenda.objects.filter(AgePrio='C')
    if AgeFiltro == 'SP': list_comp = ClAgenda.objects.filter(AgePrio='P')
    context = {'AgeFiltro':AgeFiltro, 'list_comp':list_comp}
    return HttpResponse(template.render(context,request))
