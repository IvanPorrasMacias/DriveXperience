# Generated by Django 5.1.1 on 2024-10-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_vehículo_enganche'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='comisionApertura',
            field=models.DecimalField(decimal_places=2, default=5000.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plan',
            name='seguro',
            field=models.DecimalField(decimal_places=2, default=12000.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='plan',
            name='interes',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=5),
        ),
    ]
