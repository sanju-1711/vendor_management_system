# Generated by Django 5.0.4 on 2024-05-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_historical_performance_average_response_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='avg_response_time',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fulfillment_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(null=True),
        ),
    ]
