# Generated by Django 3.1.5 on 2022-05-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jai_Kisan', '0006_auto_20220527_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Tracter', 'Tracter'), ('Boring Machine', 'Boring Machine'), ('Harvestor', 'Harvestor'), ('Cultivator', 'Cultivater'), ('Drones', 'Drones')], max_length=20),
        ),
        migrations.AlterField(
            model_name='vendorproduct',
            name='category',
            field=models.CharField(choices=[('Tracter', 'Tracter'), ('Boring Machine', 'Boring Machine'), ('Harvestor', 'Harvestor'), ('Cultivator', 'Cultivater'), ('Drones', 'Drones')], max_length=20),
        ),
    ]