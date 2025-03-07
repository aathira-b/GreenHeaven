# Generated by Django 5.1.4 on 2025-01-26 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_tbl_shop'),
        ('Shop', '0011_delete_tbl_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_content', models.CharField(max_length=500)),
                ('chat_time', models.DateTimeField()),
                ('chat_file', models.FileField(upload_to='ChatFiles/')),
                ('designer_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_designer', to='Guest.tbl_designer')),
                ('designer_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_designer', to='Guest.tbl_designer')),
                ('shop_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_shop', to='Guest.tbl_shop')),
                ('shop_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_shop', to='Guest.tbl_shop')),
                ('user_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='Guest.tbl_user')),
                ('user_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='Guest.tbl_user')),
            ],
        ),
    ]
