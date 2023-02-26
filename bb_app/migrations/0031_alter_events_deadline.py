# Generated by Django 3.2 on 2023-02-25 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0030_alter_events_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 25, 23, 23, 37, 904788), help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
    ]