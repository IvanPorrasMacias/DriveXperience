# Generated by Django 5.1.1 on 2024-10-07 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descuento', models.IntegerField()),
                ('vehículo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.vehículo')),
            ],
        ),
    ]
