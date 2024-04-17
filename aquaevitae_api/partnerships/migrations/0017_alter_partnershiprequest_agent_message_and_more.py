# Generated by Django 4.2.7 on 2024-04-17 00:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("partnerships", "0016_alter_partnershiprequest_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partnershiprequest",
            name="agent_message",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="partnershiprequest",
            name="agent_role",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="partnershiprequest",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region=None
            ),
        ),
    ]
