# Generated by Django 5.0.4 on 2024-04-14 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klub_100kilo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='diet',
            table='Diet',
        ),
        migrations.AlterModelTable(
            name='measurements',
            table='Measurements',
        ),
        migrations.AlterModelTable(
            name='reservations',
            table='Reservations',
        ),
    ]