# Generated by Django 4.2.7 on 2024-03-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recommendations", "0011_formskindisease_level_alter_formskintype_skin_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="is_deleted",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]