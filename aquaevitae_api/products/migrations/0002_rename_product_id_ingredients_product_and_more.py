# Generated by Django 4.2.7 on 2023-11-30 17:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ingredients",
            old_name="product_id",
            new_name="product",
        ),
        migrations.RenameField(
            model_name="skintype",
            old_name="product_id",
            new_name="product",
        ),
        migrations.RenameField(
            model_name="type",
            old_name="product_id",
            new_name="product",
        ),
    ]
