# Generated by Django 2.0.2 on 2018-03-05 07:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20180305_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 5, 7, 55, 20, 763888, tzinfo=utc), verbose_name='Edit time'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 5, 7, 55, 20, 763888, tzinfo=utc), verbose_name='publish time'),
        ),
    ]
