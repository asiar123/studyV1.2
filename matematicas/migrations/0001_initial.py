# Generated by Django 3.2 on 2023-07-04 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Math',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matematicas1', models.CharField(max_length=100, null=True)),
                ('Matematicas2', models.CharField(max_length=100, null=True)),
                ('Matematicas3', models.CharField(max_length=100, null=True)),
                ('Matematicas4', models.CharField(max_length=100, null=True)),
                ('Matematicas5', models.CharField(max_length=100, null=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person.persona')),
            ],
            options={
                'verbose_name': 'materia',
                'verbose_name_plural': 'materias',
            },
        ),
    ]
