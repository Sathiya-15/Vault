# Generated by Django 4.2.6 on 2024-01-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="userlogin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.EmailField(blank=True, max_length=100, null=True)),
                ("password", models.CharField(blank=True, max_length=50, null=True)),
                ("firstname", models.CharField(blank=True, max_length=100, null=True)),
                ("lastname", models.CharField(blank=True, max_length=100, null=True)),
                ("mobilenumber", models.BigIntegerField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="userimages/"),
                ),
            ],
        ),
    ]
