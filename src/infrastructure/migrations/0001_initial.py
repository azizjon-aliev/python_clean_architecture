# Generated by Django 4.2.6 on 2023-10-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Currency",
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
                ("code", models.CharField(max_length=10, verbose_name="Код")),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("symbol", models.CharField(max_length=10, verbose_name="Символ")),
            ],
            options={
                "verbose_name": "Валюта",
                "verbose_name_plural": "Валюты",
            },
        ),
    ]
