# Generated by Django 4.1.3 on 2023-01-13 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aichiworks', '0005_alter_message_message_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='process_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 15, 53, 51, 838955)),
        ),
        migrations.AlterField(
            model_name='process',
            name='process_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 15, 53, 51, 837362)),
        ),
    ]
