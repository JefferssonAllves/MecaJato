# Generated by Django 5.0.7 on 2025-02-07 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Servicos',
            new_name='Servico',
        ),
    ]
