# Generated by Django 3.0 on 2021-02-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_purchasedpackage_last_benefit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedpackage',
            name='invest_amount',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
