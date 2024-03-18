# Generated by Django 4.2.7 on 2024-03-07 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "recommendations",
            "0007_form_informed_age_form_perceived_age_form_user_email_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="formskindisease",
            name="skin_disease",
            field=models.SmallIntegerField(
                choices=[
                    (1, "Translucency"),
                    (2, "Eye Area"),
                    (3, "Uniformness"),
                    (4, "Redness"),
                    (5, "Sagging"),
                    (6, "Wrinkles"),
                    (7, "Acne"),
                    (8, "Hydration"),
                    (9, "Pigmentation"),
                    (10, "Blackhead"),
                    (11, "Pores"),
                ]
            ),
        ),
    ]