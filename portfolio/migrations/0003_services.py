# Generated by Django 5.0.7 on 2024-07-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_blogs"),
    ]

    operations = [
        migrations.CreateModel(
            name="services",
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
                ("title", models.CharField(max_length=60)),
                ("description", models.TextField()),
            ],
        ),
    ]
