from django.urls import path
from AppAgenda import views

#O path cria um caminho, mas como o caminho está vazio o AppAgenda import o views e abre a aplicação.
urlpatterns = [path('',views.index,name='index'),
               path('<AgeFiltro>', views.compromissos, name='compromissos')]
