# Generated by Django 4.2.7 on 2023-11-30 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("partnerships", "0001_initial"),
        ("products", "0001_initial"),
        ("companies", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductRequest",
            fields=[
                (
                    "product_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="products.product",
                    ),
                ),
                ("approved_date", models.DateTimeField(blank=True, null=True)),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("A", "Approved"), ("W", "Waiting"), ("D", "Denied")],
                        max_length=1,
                    ),
                ),
                (
                    "partnership",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="products",
                        to="partnerships.partnership",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("products.product", models.Model),
        ),
        migrations.AddField(
            model_name="partnership",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="companies.company",
            ),
        ),
        migrations.AddField(
            model_name="partnership",
            name="company_request",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="partnerships.companyrequest",
            ),
        ),
    ]
