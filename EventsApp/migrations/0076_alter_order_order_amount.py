# Generated by Django 3.2.12 on 2022-09-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsApp', '0075_alter_orderitems_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_amount',
            field=models.FloatField(),
        ),
    ]
