# Generated by Django 3.2.9 on 2021-11-23 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appliction', '0016_alter_repayment_loan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repayment',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='repayment',
            name='loan_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='appliction.loanapplication'),
        ),
    ]
