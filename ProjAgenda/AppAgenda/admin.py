from django.contrib import admin
from AppAgenda.models import ClAgenda

class ClAgendaAdmin(admin.ModelAdmin):pass # Se coloca o pass, o admin vai construir de acordo com o padrão dele.
#É esse comando abaixo que vai criar o site.
admin.site.register(ClAgenda,ClAgendaAdmin) # Ele vai registrar o ClAgenda criado no model com o ClAgendaAdmin.

