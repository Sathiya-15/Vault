# Generated by Django 5.0.1 on 2024-03-22 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_emailotp_alter_userlogin_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 22, 11, 13, 48, 322846), null=True),
        ),
        migrations.DeleteModel(
            name='attendence',
        ),
    ]
