# Generated by Django 2.1.4 on 2019-01-09 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190109_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 9, 17, 20, 29, 287998), verbose_name='date published'),
        ),
    ]