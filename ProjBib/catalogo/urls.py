from django.urls import path
from catalogo import views

urlpatterns= [
    path('', views.index, name='index'),
    path('livros', views.livros,name='livros')
]
