# Generated by Django 4.2.7 on 2024-04-17 01:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recommendations", "0015_form_autorized"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formskindisease",
            name="level",
            field=models.SmallIntegerField(
                choices=[(0, "None"), (1, "Low"), (2, "Medium"), (3, "High")]
            ),
        ),
    ]
