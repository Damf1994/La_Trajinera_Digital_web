# Generated by Django 3.0.3 on 2020-06-08 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_usercliente_tipo_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercliente',
            name='tipo_usuario',
        ),
    ]
