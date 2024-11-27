from django.contrib import admin
from AppEnc.models import ClCandidato,ClEsporte,ClMusica,ClFesta,ClCultura,ClEstudo

class ClEsporteadmin(admin.ModelAdmin):pass
admin.site.register(ClEsporte,ClEsporteadmin)

class ClCandidatoadmin(admin.ModelAdmin):pass
admin.site.register(ClCandidato,ClCandidatoadmin)

class ClMusicaadmin(admin.ModelAdmin):pass
admin.site.register(ClMusica,ClMusicaadmin)

class ClFestaadmin(admin.ModelAdmin):pass
admin.site.register(ClFesta,ClFestaadmin)

class ClCulturaaadmin(admin.ModelAdmin):pass
admin.site.register(ClCultura,ClCulturaaadmin)

class ClEstudosadmin(admin.ModelAdmin):pass
admin.site.register(ClEstudo,ClEstudosadmin)


# Register your models here.
