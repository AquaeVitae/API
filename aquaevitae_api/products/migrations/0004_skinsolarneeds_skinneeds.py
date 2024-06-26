# Generated by Django 4.2.7 on 2024-03-14 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_price_product_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="SkinSolarNeeds",
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
                (
                    "skin_solar_need",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[
                            (1, "Body Protection"),
                            (2, "Hair Protection"),
                            (3, "Face Protection"),
                            (4, "Aftersun"),
                            (5, "Others"),
                            (6, "Suntun"),
                        ],
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skin_solar_needs",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "unique_together": {("product", "skin_solar_need")},
            },
        ),
        migrations.CreateModel(
            name="SkinNeeds",
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
                (
                    "skin_need",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[
                            (1, "Clean"),
                            (2, "Makeup Remover"),
                            (3, "Hidrate"),
                            (4, "Nourish"),
                            (5, "Soothe"),
                            (6, "Complexion Care"),
                            (7, "Repairers"),
                            (8, "Exfoliating"),
                            (9, "Aging"),
                            (10, "Acne"),
                            (11, "Marks"),
                            (12, "Irritation"),
                            (13, "Antiperspirant"),
                            (14, "Scalp"),
                            (15, "Intimate Care"),
                            (16, "Hands"),
                            (17, "Feet"),
                            (18, "Others"),
                        ],
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skin_needs",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "unique_together": {("product", "skin_need")},
            },
        ),
    ]
