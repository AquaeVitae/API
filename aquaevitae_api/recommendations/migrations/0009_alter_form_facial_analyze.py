# Generated by Django 4.2.7 on 2024-03-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recommendations", "0008_alter_formskindisease_skin_disease"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="facial_analyze",
            field=models.UUIDField(blank=True, null=True, unique=True),
        ),
    ]
