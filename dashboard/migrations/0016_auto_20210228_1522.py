# Generated by Django 3.0 on 2021-02-28 09:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20210228_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allusernotice',
            name='notice',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='purchasedpackage',
            name='last_benefit_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 28, 9, 52, 18, 382882, tzinfo=utc), null=True),
        ),
    ]
