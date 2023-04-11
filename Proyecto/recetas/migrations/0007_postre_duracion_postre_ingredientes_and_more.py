# Generated by Django 4.1.7 on 2023-04-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0006_platoprincipal_duracion_platoprincipal_ingredientes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postre',
            name='duracion',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='postre',
            name='ingredientes',
            field=models.CharField(default=' ', max_length=60),
        ),
        migrations.AddField(
            model_name='postre',
            name='procedimiento',
            field=models.CharField(default=' ', max_length=500),
        ),
        migrations.AddField(
            model_name='singluten',
            name='duracion',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='singluten',
            name='ingredientes',
            field=models.CharField(default=' ', max_length=60),
        ),
        migrations.AddField(
            model_name='singluten',
            name='procedimiento',
            field=models.CharField(default=' ', max_length=500),
        ),
        migrations.AddField(
            model_name='vegano',
            name='duracion',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='vegano',
            name='ingredientes',
            field=models.CharField(default=' ', max_length=60),
        ),
        migrations.AddField(
            model_name='vegano',
            name='procedimiento',
            field=models.CharField(default=' ', max_length=500),
        ),
    ]