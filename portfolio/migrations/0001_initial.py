# Generated by Django 5.0.7 on 2024-07-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=10)),
                ("description", models.TextField()),
            ],
        ),
    ]
