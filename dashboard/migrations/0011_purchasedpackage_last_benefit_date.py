# Generated by Django 3.0 on 2021-02-28 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20210228_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedpackage',
            name='last_benefit_date',
            field=models.DateField(blank=True, default=datetime.date(2021, 2, 28), null=True),
        ),
    ]
