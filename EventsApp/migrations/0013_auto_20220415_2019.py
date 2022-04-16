# Generated by Django 3.2.12 on 2022-04-16 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsApp', '0012_alter_venues_vm_venue_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venues',
            name='vm_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='venues',
            name='vm_venue_country',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='venues',
            name='vm_venue_description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='venues',
            name='vm_venue_province',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='venues',
            name='vm_venue_street',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='venues',
            name='vm_venue_zip',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='venues',
            name='vm_venuecity',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
