# Generated by Django 5.1.7 on 2025-04-07 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_tbl_shop'),
        ('Shop', '0014_tbl_chat'),
        ('User', '0020_tbl_booking_tbl_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='Guest.tbl_user')),
            ],
            options={
                'unique_together': {('user', 'product')},
            },
        ),
    ]
