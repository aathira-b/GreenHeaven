# Generated by Django 5.1.3 on 2024-12-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_content', models.CharField(max_length=30)),
                ('feedback_date', models.CharField(max_length=30)),
            ],
        ),
    ]
