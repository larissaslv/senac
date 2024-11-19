# Generated by Django 5.1.2 on 2024-11-12 18:03

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClAutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(help_text='Nome do Autor', max_length=50, verbose_name='Autor')),
                ('dtnasc', models.DateField(blank=True, null=True, verbose_name='Nascimento')),
                ('dtmort', models.DateField(blank=True, null=True, verbose_name='Morte')),
            ],
            options={
                'ordering': ['autor'],
            },
        ),
        migrations.CreateModel(
            name='ClEditora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editora', models.CharField(help_text='Nome da Editora', max_length=50)),
            ],
            options={
                'ordering': ['editora'],
            },
        ),
        migrations.CreateModel(
            name='ClLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titul', models.CharField(help_text='Nome do livro', max_length=50, verbose_name='Título')),
                ('descr', models.CharField(help_text='Descrição do livro', max_length=500, verbose_name='Descrição')),
                ('categ', models.CharField(blank=True, choices=[('F', 'Ficção'), ('R', 'Romance'), ('D', 'Drama'), ('A', 'Aventura'), ('T', 'Técnico'), ('I', 'Indefinido')], default='I', help_text='Status do livro', max_length=1, verbose_name='Categoria')),
                ('autor', models.ForeignKey(help_text='Autor do livro', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.clautor')),
                ('edito', models.ForeignKey(help_text='Editora do Livro', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.cleditora')),
            ],
            options={
                'ordering': ['titul'],
            },
        ),
        migrations.CreateModel(
            name='ClExemplar',
            fields=[
                ('registro', models.UUIDField(default=uuid.uuid4, help_text='Registro único para esse exemplar', primary_key=True, serialize=False)),
                ('detalhes', models.CharField(help_text='Detalhes do exemplar', max_length=50)),
                ('retorno', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('M', 'Manutenção'), ('D', 'Disponível'), ('R', 'Retirado')], default='M', help_text='Status do exemplar', max_length=1)),
                ('livro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.cllivro')),
            ],
            options={
                'ordering': ['retorno'],
            },
        ),
    ]
