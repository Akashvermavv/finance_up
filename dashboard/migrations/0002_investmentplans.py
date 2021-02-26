# Generated by Django 3.0 on 2021-02-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentPlans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(choices=[('starter', 'Starter'), ('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum'), ('diamond', 'Diamond'), ('vip', 'VIP')], max_length=150)),
                ('invest_start', models.BigIntegerField()),
                ('invest_end', models.BigIntegerField()),
                ('daily_earn_per', models.FloatField()),
                ('total_days', models.IntegerField()),
                ('total_earn_in_per', models.FloatField()),
                ('sponsor_bonus_in_per', models.FloatField()),
                ('matching_bonus_in_per', models.FloatField()),
                ('daily_cap_price', models.BigIntegerField()),
            ],
        ),
    ]