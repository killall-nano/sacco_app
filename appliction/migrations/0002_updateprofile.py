# Generated by Django 3.2.9 on 2021-11-19 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appliction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('member', 'member'), ('staff', 'staff'), ('guest', 'guest')], default='guest', max_length=20)),
                ('id_number', models.PositiveSmallIntegerField()),
                ('address', models.CharField(blank=True, max_length=200)),
                ('phone_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]