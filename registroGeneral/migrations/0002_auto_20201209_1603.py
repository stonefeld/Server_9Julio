# Generated by Django 3.1.4 on 2020-12-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroGeneral', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradageneral',
            name='entra',
        ),
        migrations.RemoveField(
            model_name='entradageneral',
            name='sale',
        ),
        migrations.AddField(
            model_name='entradageneral',
            name='direccion',
            field=models.CharField(default='ENTRADA', max_length=30),
        ),
    ]