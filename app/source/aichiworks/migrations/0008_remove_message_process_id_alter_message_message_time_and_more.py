# Generated by Django 4.1.3 on 2023-02-10 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aichiworks', '0007_alter_message_message_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='process_id',
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 10, 19, 40, 24, 749881)),
        ),
        migrations.AlterField(
            model_name='process',
            name='process_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 10, 19, 40, 24, 748499)),
        ),
    ]
