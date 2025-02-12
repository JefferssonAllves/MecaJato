# Generated by Django 5.0.7 on 2025-02-05 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carro', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=8)),
                ('ano', models.IntegerField()),
                ('lavagens', models.IntegerField(default=0)),
                ('consertos', models.IntegerField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]
