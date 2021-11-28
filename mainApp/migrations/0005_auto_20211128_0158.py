# Generated by Django 3.2.9 on 2021-11-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_alter_servicecategory_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='selected_addOns',
            field=models.TextField(default='..'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='Total_amount_of_order',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
