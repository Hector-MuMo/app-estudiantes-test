# Generated by Django 2.2.24 on 2021-10-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('apellido', models.CharField(default='', max_length=200)),
                ('direccion', models.CharField(default='', max_length=250)),
                ('matricula', models.IntegerField(default=None, null=True)),
                ('activo', models.BooleanField(default=False)),
                ('semestre', models.CharField(default='', max_length=50)),
            ],
        ),
    ]