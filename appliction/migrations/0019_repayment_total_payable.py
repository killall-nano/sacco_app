# Generated by Django 3.2.9 on 2021-11-23 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliction', '0018_repayment_intrest'),
    ]

    operations = [
        migrations.AddField(
            model_name='repayment',
            name='total_payable',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
