# Generated by Django 5.1.7 on 2025-03-07 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0018_delete_tbl_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_cart',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='tbl_cart',
            name='product',
        ),
        migrations.DeleteModel(
            name='tbl_booking',
        ),
        migrations.DeleteModel(
            name='tbl_cart',
        ),
    ]
