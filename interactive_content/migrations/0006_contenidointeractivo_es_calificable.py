# Generated by Django 2.2.4 on 2020-05-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactive_content', '0005_contenidointeractivo_puedesaltar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenidointeractivo',
            name='es_calificable',
            field=models.BooleanField(default=False),
        ),
    ]
