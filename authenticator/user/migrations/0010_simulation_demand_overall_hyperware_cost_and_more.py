# Generated by Django 5.0.1 on 2024-01-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_simulation_demand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation_demand',
            name='Overall_Hyperware_cost',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='simulation_demand',
            name='Overall_Metware_cost',
            field=models.BigIntegerField(default=None),
        ),
    ]
