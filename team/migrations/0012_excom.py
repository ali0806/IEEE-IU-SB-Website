# Generated by Django 4.1.7 on 2023-06-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0011_alter_contact_message"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExCom",
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
                ("photo", models.ImageField(upload_to="Excom_photo")),
                ("name", models.CharField(max_length=100)),
                ("message", models.CharField(default=" ", max_length=1000, null=True)),
                ("title", models.CharField(max_length=300)),
            ],
        ),
    ]
