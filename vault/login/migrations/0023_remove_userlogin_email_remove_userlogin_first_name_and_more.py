# Generated by Django 5.0.1 on 2024-02-16 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0022_alter_userlogin_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogin',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userlogin',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userlogin',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 16, 12, 41, 7, 562556), null=True),
        ),
    ]