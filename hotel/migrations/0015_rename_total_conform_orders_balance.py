# Generated by Django 3.2 on 2021-06-12 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0014_conform_orders_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conform_orders',
            old_name='total',
            new_name='balance',
        ),
    ]
