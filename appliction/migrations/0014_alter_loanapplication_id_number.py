# Generated by Django 3.2.9 on 2021-11-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliction', '0013_remove_loanapplication_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='id_number',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
