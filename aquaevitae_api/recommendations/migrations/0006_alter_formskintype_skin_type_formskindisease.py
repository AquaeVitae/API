# Generated by Django 4.2.7 on 2024-03-07 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("recommendations", "0005_form_facial_analyze_alter_formskintype_skin_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formskintype",
            name="skin_type",
            field=models.SmallIntegerField(
                choices=[
                    ("<enum.auto object at 0x7fb3bd9fc970>", "Dry"),
                    ("<enum.auto object at 0x7fb3bd9fc610>", "Sensitive"),
                    ("<enum.auto object at 0x7fb3bd9fcd00>", "Sensible"),
                    ("<enum.auto object at 0x7fb3bd9fcd90>", "Extra Dry"),
                    ("<enum.auto object at 0x7fb3bd9fce20>", "Combined"),
                    ("<enum.auto object at 0x7fb3bd9fd4b0>", "Irritated"),
                    ("<enum.auto object at 0x7fb3bd9fd540>", "Normal"),
                    ("<enum.auto object at 0x7fb3bd9fd5d0>", "Atopic Tendency"),
                    ("<enum.auto object at 0x7fb3bd9fd660>", "Fragile Damaged"),
                    ("-1", "NOT_SURE"),
                ],
                default="-1",
            ),
        ),
        migrations.CreateModel(
            name="FormSkinDisease",
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
                    "skin_disease",
                    models.SmallIntegerField(
                        choices=[
                            ("<enum.auto object at 0x7fb3bd9fc970>", "Translucency"),
                            ("<enum.auto object at 0x7fb3bd9fcd90>", "Eye Area"),
                            ("<enum.auto object at 0x7fb3bd9fd540>", "Uniformness"),
                            ("<enum.auto object at 0x7fb3bd9fe590>", "Redness"),
                            ("<enum.auto object at 0x7fb3bd9ffbe0>", "Sagging"),
                            ("<enum.auto object at 0x7fb3bd9ffbb0>", "Wrinkles"),
                            ("<enum.auto object at 0x7fb3bd9ffb20>", "Acne"),
                            ("<enum.auto object at 0x7fb3bd9ffa90>", "Hydration"),
                            ("<enum.auto object at 0x7fb3bd9ffa00>", "Pigmentation"),
                            ("<enum.auto object at 0x7fb3bd9ff970>", "Blackhead"),
                            ("<enum.auto object at 0x7fb3bd9ff8e0>", "Pores"),
                        ]
                    ),
                ),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skin_diseases",
                        to="recommendations.form",
                    ),
                ),
            ],
            options={
                "unique_together": {("form", "skin_disease")},
            },
        ),
    ]
