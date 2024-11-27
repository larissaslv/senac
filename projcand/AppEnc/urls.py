from django.urls import path
from AppEnc import views

urlpatterns = [path('',views.index,name='index'),
               path('esp/<tipo>',views.sel_esporte, name='sel_esporte'),
               path('mus/<tipo>',views.sel_musica, name='sel_musica'),
               path('fest/<tipo>',views.sel_festa, name='sel_festa'),
               path('est/<tipo>',views.sel_estudo, name='sel_estudo'),
               path('cult/<tipo>',views.sel_cultura, name='sel_cultura')]
