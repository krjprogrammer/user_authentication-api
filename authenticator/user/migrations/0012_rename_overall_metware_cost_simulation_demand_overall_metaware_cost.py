# Generated by Django 5.0.1 on 2024-01-23 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_simulation_demand_overall_hyperware_cost_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simulation_demand',
            old_name='Overall_Metware_cost',
            new_name='Overall_Metaware_cost',
        ),
    ]
