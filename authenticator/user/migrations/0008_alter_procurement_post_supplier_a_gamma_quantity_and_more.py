# Generated by Django 5.0.1 on 2024-01-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_procurement_post_supplier_a_gamma_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_A_Gamma_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_B_Delta_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_B_Gamma_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_C_Delta_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_C_Gamma_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_D_Delta_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_D_Epsilon_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_D_Gamma_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_E_Delta_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_E_Epsilon_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_F_Delta_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_F_Epsilon_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='procurement_post',
            name='Supplier_G_Epsilon_Quantity',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
    ]
