# Generated by Django 2.0.7 on 2018-08-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('tipo_usuario', models.IntegerField(default=0)),
            ],
        ),
    ]
