# Generated by Django 3.1.2 on 2020-11-05 14:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuariosistema', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Perfil',
        ),
    ]
