# Generated by Django 5.0.1 on 2024-01-30 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_userlogin_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 30, 10, 12, 29, 302624), null=True),
        ),
    ]
