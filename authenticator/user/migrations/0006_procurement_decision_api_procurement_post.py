# Generated by Django 5.0.1 on 2024-01-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_product_config'),
    ]

    operations = [
        migrations.CreateModel(
            name='procurement_decision_api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_ID', models.IntegerField()),
                ('simulation_id', models.IntegerField()),
                ('firm_id', models.IntegerField()),
                ('Quarter', models.IntegerField()),
                ('SAC_Responses', models.JSONField()),
                ('Alpha', models.JSONField()),
                ('Beta', models.JSONField()),
                ('Gamma', models.JSONField()),
                ('Delta', models.JSONField()),
                ('Epsilon', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='procurement_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_ID', models.IntegerField()),
                ('simulation_id', models.IntegerField()),
                ('firm_id', models.IntegerField()),
                ('Quarter', models.IntegerField()),
                ('SAC_Responses', models.JSONField()),
                ('Alpha_quantity', models.BigIntegerField()),
                ('Beta_quantity', models.BigIntegerField()),
                ('Supplier_A_Gamma_Quantity', models.BigIntegerField()),
                ('Supplier_B_Gamma_Quantity', models.BigIntegerField()),
                ('Supplier_C_Gamma_Quantity', models.BigIntegerField()),
                ('Supplier_D_Gamma_Quantity', models.BigIntegerField()),
                ('Supplier_B_Delta_Quantity', models.BigIntegerField()),
                ('Supplier_C_Delta_Quantity', models.BigIntegerField()),
                ('Supplier_D_Delta_Quantity', models.BigIntegerField()),
                ('Supplier_E_Delta_Quantity', models.BigIntegerField()),
                ('Supplier_F_Delta_Quantity', models.BigIntegerField()),
                ('Supplier_D_Epsilon_Quantity', models.BigIntegerField()),
                ('Supplier_E_Epsilon_Quantity', models.BigIntegerField()),
                ('Supplier_F_Epsilon_Quantity', models.BigIntegerField()),
                ('Supplier_G_Epsilon_Quantity', models.BigIntegerField()),
            ],
        ),
    ]