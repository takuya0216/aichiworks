# Generated by Django 4.1.3 on 2023-01-13 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aichiworks', '0004_rename_process_type_id_process_status_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 15, 52, 18, 585162)),
        ),
        migrations.AlterField(
            model_name='process',
            name='process_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 15, 52, 18, 583798)),
        ),
    ]