# Generated by Django 5.0.4 on 2024-05-05 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_details', models.TextField(max_length=500)),
                ('address', models.TextField(max_length=10000)),
                ('vendor_code', models.CharField(max_length=10, unique=True)),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('avg_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=10, unique=True)),
                ('order_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('quality_rating', models.FloatField()),
                ('issue_date', models.DateTimeField()),
                ('acknowledgement_date', models.DateTimeField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Historical_Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendor')),
            ],
        ),
    ]
