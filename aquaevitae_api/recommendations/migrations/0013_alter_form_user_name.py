# Generated by Django 4.2.7 on 2024-03-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recommendations", "0012_alter_form_is_deleted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="user_name",
            field=models.CharField(default="user", max_length=50),
            preserve_default=False,
        ),
    ]
