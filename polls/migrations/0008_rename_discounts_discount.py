# Generated by Django 4.1.dev20211206065911 on 2021-12-10 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_rename_customers_customer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Discounts',
            new_name='Discount',
        ),
    ]
