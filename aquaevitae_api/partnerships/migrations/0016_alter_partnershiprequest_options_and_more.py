# Generated by Django 4.2.7 on 2024-03-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("partnerships", "0015_alter_partnershiprequest_country"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="partnershiprequest",
            options={"verbose_name": "Partnership Request"},
        ),
        migrations.AlterField(
            model_name="partnershiprequest",
            name="comments",
            field=models.TextField(null=True),
        ),
    ]
