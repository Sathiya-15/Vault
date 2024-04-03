# Generated by Django 5.0.1 on 2024-03-29 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0027_rename_userlogin_attendence_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='log_in_at',
            new_name='login_at',
        ),
        migrations.RenameField(
            model_name='attendence',
            old_name='log_out_at',
            new_name='logout_at',
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 29, 12, 26, 39, 90238), null=True),
        ),
    ]