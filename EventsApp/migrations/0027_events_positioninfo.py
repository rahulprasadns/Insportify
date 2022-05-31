# Generated by Django 3.2.12 on 2022-05-17 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EventsApp', '0026_delete_eventsapptestcity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events_PositionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_number', models.IntegerField(blank=True, null=True)),
                ('max_age', models.IntegerField(blank=True, null=True)),
                ('min_age', models.IntegerField(blank=True, null=True)),
                ('no_of_position', models.IntegerField(blank=True, null=True)),
                ('position_cost', models.IntegerField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventsApp.master_table')),
            ],
        ),
    ]