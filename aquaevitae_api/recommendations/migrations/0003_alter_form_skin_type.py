# Generated by Django 4.2.7 on 2024-03-07 15:25

import aquaevitae_api.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recommendations", "0002_alter_form_skin_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="skin_type",
            field=aquaevitae_api.models.fields.SetField(
                base_field=models.SmallIntegerField(
                    choices=[
                        ("<enum.auto object at 0x7f958ddfc970>", "Dry"),
                        ("<enum.auto object at 0x7f958ddfc610>", "Sensitive"),
                        ("<enum.auto object at 0x7f958ddfcd00>", "Sensible"),
                        ("<enum.auto object at 0x7f958ddfcd90>", "Extra Dry"),
                        ("<enum.auto object at 0x7f958ddfce20>", "Combined"),
                        ("<enum.auto object at 0x7f958ddfd4b0>", "Irritated"),
                        ("<enum.auto object at 0x7f958ddfd540>", "Normal"),
                        ("<enum.auto object at 0x7f958ddfd5d0>", "Atopic Tendency"),
                        ("<enum.auto object at 0x7f958ddfd690>", "Fragile Damaged"),
                        ("-1", "All"),
                    ],
                    default="-1",
                ),
                default=list,
                size=10,
            ),
        ),
    ]
