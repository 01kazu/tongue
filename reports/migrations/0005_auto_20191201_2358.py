# Generated by Django 2.2.1 on 2019-12-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20191201_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]
