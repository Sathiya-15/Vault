# Generated by Django 5.0.1 on 2024-02-14 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_userlogin_role_alter_userlogin_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_in_at', models.TimeField()),
                ('log_out_at', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 14, 15, 58, 42, 598826), null=True),
        ),
    ]
