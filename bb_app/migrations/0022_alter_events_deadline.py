# Generated by Django 3.2 on 2021-08-07 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0021_auto_20210805_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 20, 18, 21, 554568), help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
    ]
