# Generated by Django 5.0.1 on 2024-03-22 06:12

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_alter_userlogin_created_at_delete_attendence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 22, 11, 42, 23, 728066), null=True),
        ),
        migrations.CreateModel(
            name='attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_in_at', models.DateTimeField()),
                ('log_out_at', models.DateTimeField(blank=True, null=True)),
                ('userlogin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]