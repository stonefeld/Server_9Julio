# Generated by Django 3.1.7 on 2021-03-22 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('estacionamiento', '0003_auto_20210319_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroestacionamiento',
            name='identificador',
            field=models.CharField(default='Error', max_length=30, verbose_name='Identificador'),
        ),
        migrations.AlterField(
            model_name='registroestacionamiento',
            name='noSocio',
            field=models.IntegerField(blank=True, null=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='registroestacionamiento',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.persona', verbose_name='Persona'),
        ),
        migrations.AlterField(
            model_name='registroestacionamiento',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estacionamiento.proveedor', verbose_name='Proveedor'),
        ),
    ]