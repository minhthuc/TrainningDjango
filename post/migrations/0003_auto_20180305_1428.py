# Generated by Django 2.0.2 on 2018-03-05 07:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20180305_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 5, 7, 28, 2, 967208, tzinfo=utc), verbose_name='publish time'),
        ),
    ]