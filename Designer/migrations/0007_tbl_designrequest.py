# Generated by Django 5.1.3 on 2024-12-20 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Designer', '0006_tbl_gallery'),
        ('Guest', '0006_tbl_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_designrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designrequest_date', models.CharField(max_length=30)),
                ('designrequest_todate', models.CharField(max_length=30)),
                ('designrequest_status', models.IntegerField(default=0)),
                ('designrequest_amount', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Designer.tbl_work')),
            ],
        ),
    ]
