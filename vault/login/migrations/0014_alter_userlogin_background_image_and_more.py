# Generated by Django 5.0.1 on 2024-02-07 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_rename_postalcode_userlogin_pincode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='Background_image',
            field=models.ImageField(blank=True, default='userimages/default_back.png', null=True, upload_to='userimages/'),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='Profile_image',
            field=models.ImageField(blank=True, default='userimages/default_profile.png', null=True, upload_to='userimages/'),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 7, 13, 37, 48, 655493), null=True),
        ),
    ]
