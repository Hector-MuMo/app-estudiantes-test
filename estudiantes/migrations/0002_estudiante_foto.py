# Generated by Django 2.2.24 on 2021-10-31 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
