# Generated by Django 4.2.7 on 2024-04-17 00:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "recommendations",
            "0014_remove_form_facial_analyze_remove_form_perceived_age_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="form",
            name="autorized",
            field=models.BooleanField(default=False),
        ),
    ]
