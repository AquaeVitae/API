# Generated by Django 4.2.7 on 2024-03-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("partnerships", "0011_alter_partnershiprequest_phone"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="partnershiprequest",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="partnershiprequest",
            name="agent_email",
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name="partnershiprequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("A", "Approved"),
                    ("W", "Waiting"),
                    ("D", "Denied"),
                    ("S", "Denied by Server"),
                ],
                max_length=1,
            ),
        ),
        migrations.AlterModelTable(
            name="partnershiprequest",
            table="partnership_request",
        ),
    ]