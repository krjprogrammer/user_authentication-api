# Generated by Django 5.0.1 on 2024-01-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_procurement_post_supplier_a_gamma_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='simulation_demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_ID', models.IntegerField()),
                ('simulation_id', models.IntegerField()),
                ('firm_id', models.IntegerField()),
                ('Quarter', models.IntegerField()),
                ('Rules', models.JSONField()),
                ('Hyperware', models.BigIntegerField()),
                ('Metaware', models.BigIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_A_Gamma_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_B_Delta_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_B_Gamma_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_C_Delta_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_C_Gamma_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_D_Delta_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_D_Epsilon_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_D_Gamma_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_E_Delta_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_E_Epsilon_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_F_Delta_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_F_Epsilon_Quantity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_G_Epsilon_Quantity',
            field=models.BigIntegerField(null=True),
        ),
    ]
