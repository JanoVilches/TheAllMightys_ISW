# Generated by Django 2.0.7 on 2018-08-01 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0004_solicitar_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitar_material',
            name='material',
        ),
        migrations.DeleteModel(
            name='Solicitar_Material',
        ),
    ]
