# Generated by Django 5.1.3 on 2024-12-12 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0005_tbl_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_email', models.CharField(max_length=30)),
                ('user_contact', models.CharField(max_length=30)),
                ('user_address', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=30)),
                ('user_photo', models.FileField(upload_to='Assets/User/Photo/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
