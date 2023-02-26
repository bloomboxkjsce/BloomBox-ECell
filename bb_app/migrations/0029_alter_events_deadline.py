# Generated by Django 3.2 on 2023-02-15 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0028_alter_events_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 16, 1, 48, 50, 204865), help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
    ]