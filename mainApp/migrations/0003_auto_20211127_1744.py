# Generated by Django 3.2.9 on 2021-11-27 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_bookings_service_servicecategory_servicecategoryaddons'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecategory',
            name='info',
            field=models.TextField(default='More About this Product Like it Description'),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='duration',
            field=models.TextField(max_length=500),
        ),
    ]
