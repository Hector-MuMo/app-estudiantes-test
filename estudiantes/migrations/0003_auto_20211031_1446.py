# Generated by Django 2.2.24 on 2021-10-31 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0002_estudiante_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(default='', max_length=100)),
                ('semestre', models.CharField(default='', max_length=100)),
                ('formacion', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
