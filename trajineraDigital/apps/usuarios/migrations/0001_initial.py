# Generated by Django 3.0.3 on 2020-06-06 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=8)),
            ],
        ),
    ]