# Generated by Django 5.0.1 on 2024-02-07 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_alter_userlogin_background_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='Role',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 7, 17, 38, 53, 408974), null=True),
        ),
    ]
