# Generated by Django 4.2.7 on 2024-03-27 19:10

import analysis.models.facial_analysis
import django.core.files.storage
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("analysis", "0002_delete_facialanalysis"),
    ]

    operations = [
        migrations.CreateModel(
            name="FacialAnalysis",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(blank=True, default=False)),
                (
                    "image",
                    models.ImageField(
                        storage=django.core.files.storage.FileSystemStorage(
                            "/home/guitonello/tese/aquaevitae/api/aquaevitae_api/analysis/images"
                        ),
                        unique=True,
                        upload_to=analysis.models.facial_analysis.upload_to,
                    ),
                ),
                ("autorized_to_store", models.BooleanField(default=False)),
                ("is_done", models.BooleanField(default=False)),
                (
                    "estimated_age",
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                ("error", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Facial Analysis",
                "db_table": "facial_analysis",
            },
        ),
        migrations.CreateModel(
            name="Predictions",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "prediction_type",
                    models.PositiveSmallIntegerField(choices=[(1, "Wrinkles")]),
                ),
                (
                    "value",
                    models.FloatField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(1),
                        ],
                    ),
                ),
                (
                    "analysis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="predictions",
                        to="analysis.facialanalysis",
                    ),
                ),
            ],
            options={
                "unique_together": {("analysis", "prediction_type")},
            },
        ),
    ]
