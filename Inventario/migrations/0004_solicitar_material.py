# Generated by Django 2.0.7 on 2018-08-01 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0003_auto_20180731_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitar_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_orden', models.CharField(max_length=50, null=True)),
                ('fecha_termino', models.DateField()),
                ('cantidad_material', models.IntegerField(default=0, null=True)),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventario.Material')),
            ],
        ),
    ]
