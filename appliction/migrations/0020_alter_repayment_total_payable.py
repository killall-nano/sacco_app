# Generated by Django 3.2.9 on 2021-11-23 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliction', '0019_repayment_total_payable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repayment',
            name='total_payable',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
