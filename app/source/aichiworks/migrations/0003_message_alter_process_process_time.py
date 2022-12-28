# Generated by Django 4.1.3 on 2022-12-26 10:22

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('aichiworks', '0002_alter_process_employee_id_alter_process_process_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('process_id', models.UUIDField()),
                ('message_time', models.DateTimeField(default=datetime.datetime(2022, 12, 26, 19, 22, 30, 521495))),
                ('employee_id_from', models.SmallIntegerField()),
                ('employee_id_to', models.SmallIntegerField()),
                ('message_text', models.TextField()),
                ('message_enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='process',
            name='process_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 19, 22, 30, 520048)),
        ),
    ]
