# Generated by Django 2.2.4 on 2019-12-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0008_pausa'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='tipoActividad',
            field=models.IntegerField(default=0),
        ),
    ]
