# Generated by Django 5.0.2 on 2024-04-18 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_kitchens_kitchenimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrivateHouses",
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
                ("PrivateHouseName", models.CharField(max_length=100)),
                ("main_image", models.ImageField(upload_to="privateHouses/")),
                ("location", models.CharField(max_length=50)),
                ("completion_year", models.PositiveIntegerField()),
                ("timeline", models.CharField(max_length=15)),
                ("about", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="PrivateHouseImage",
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
                ("image", models.ImageField(upload_to="PrivateHouse_images/")),
                (
                    "description",
                    models.CharField(default="Your default value here", max_length=255),
                ),
                (
                    "PrivateHouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.privatehouses",
                    ),
                ),
            ],
        ),
    ]
