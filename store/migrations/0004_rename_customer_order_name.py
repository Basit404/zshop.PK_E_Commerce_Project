# Generated by Django 4.2.3 on 2023-07-20 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='name',
        ),
    ]
