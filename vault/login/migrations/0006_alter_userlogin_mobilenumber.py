# Generated by Django 4.2.6 on 2023-12-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0005_userlogin_mobilenumber_userlogin_password_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userlogin",
            name="mobilenumber",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
