# Generated by Django 2.2.24 on 2021-10-31 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0004_auto_20211031_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='estudiantes',
            field=models.ManyToManyField(related_name='clase', to='estudiantes.Estudiante'),
        ),
    ]
