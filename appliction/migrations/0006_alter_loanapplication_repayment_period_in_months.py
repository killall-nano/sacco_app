# Generated by Django 3.2.9 on 2021-11-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliction', '0005_loanapplication_repayment_period_in_months'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='repayment_period_in_months',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
