# Generated by Django 3.0.3 on 2020-06-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200613_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='categoria',
            name='foto',
            field=models.ImageField(null=True, upload_to='categorias/images/'),
        ),
    ]
