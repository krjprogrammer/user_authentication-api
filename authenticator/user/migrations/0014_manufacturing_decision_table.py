# Generated by Django 5.0.1 on 2024-01-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_procurements_fc_table_supplier_relationship_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='manufacturing_decision_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_ID', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('simulation_id', models.IntegerField()),
                ('production_product_0_units', models.IntegerField(default=None, null=True)),
                ('production_hyperware_units', models.IntegerField(default=None, null=True)),
                ('production_metaware_units', models.IntegerField(default=None, null=True)),
                ('product_0_info', models.JSONField(default=None, null=True)),
                ('product_hyperware_info', models.JSONField(default=None, null=True)),
                ('product_metaware_info', models.JSONField(default=None, null=True)),
            ],
        ),
    ]