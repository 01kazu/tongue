# Generated by Django 2.2.1 on 2019-12-01 07:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_report_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='context',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='report',
            name='slug',
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 12, 1, 7, 41, 13, 304781, tzinfo=utc)),
        ),
    ]
