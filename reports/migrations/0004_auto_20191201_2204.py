# Generated by Django 2.2.1 on 2019-12-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20191201_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
