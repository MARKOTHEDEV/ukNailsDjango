# Generated by Django 3.2.9 on 2021-11-27 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='service_category/')),
                ('name', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('duration', models.CharField(max_length=500)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.service')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategoryAddOns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=15)),
                ('Total_amount_of_order', models.DecimalField(decimal_places=2, max_digits=20)),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.servicecategory')),
            ],
        ),
    ]