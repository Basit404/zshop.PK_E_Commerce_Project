# Generated by Django 4.2.3 on 2023-07-20 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
