# Generated by Django 3.2.11 on 2022-04-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_alter_riskassessmentscore_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskassessmentscore',
            name='portfolio_amount',
            field=models.FloatField(default=1000000),
        ),
    ]