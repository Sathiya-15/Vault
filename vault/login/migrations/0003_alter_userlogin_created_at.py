# Generated by Django 4.2.6 on 2024-01-27 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0002_userlogin_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userlogin",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=django.utils.timezone.now, null=True
            ),
        ),
    ]
