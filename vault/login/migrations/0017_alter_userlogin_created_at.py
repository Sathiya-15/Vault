# Generated by Django 5.0.1 on 2024-02-14 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_attendence_alter_userlogin_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 14, 16, 18, 40, 713627), null=True),
        ),
    ]