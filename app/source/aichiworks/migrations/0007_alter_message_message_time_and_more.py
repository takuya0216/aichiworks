# Generated by Django 4.1.3 on 2023-01-16 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aichiworks', '0006_process_process_name_alter_message_message_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 16, 20, 42, 50, 818140)),
        ),
        migrations.AlterField(
            model_name='process',
            name='process_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='process',
            name='process_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 16, 20, 42, 50, 816652)),
        ),
    ]
