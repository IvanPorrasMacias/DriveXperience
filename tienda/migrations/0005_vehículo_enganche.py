# Generated by Django 5.1.1 on 2024-10-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_remove_plan_enganche'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehículo',
            name='enganche',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
