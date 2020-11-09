# Generated by Django 3.1.1 on 2020-11-04 14:58

from django.db import migrations, models
from django.utils import timezone
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
                ('nrSocio', models.IntegerField(blank=True, null=True)),
                ('nrTarjeta', models.IntegerField(blank=True, null=True)),
                ('general', models.BooleanField(default=False)),
                ('pileta', models.BooleanField(default=False)),
                ('tenis', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=30)),
                ('tiempo', models.DateTimeField(default= timezone.now)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.persona')),
            ],
        ),
    ]
