# Generated by Django 4.2.6 on 2023-12-08 08:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0003_mymodels"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userlogin",
            old_name="password",
            new_name="firstname",
        ),
        migrations.RenameField(
            model_name="userlogin",
            old_name="username",
            new_name="lastname",
        ),
    ]
