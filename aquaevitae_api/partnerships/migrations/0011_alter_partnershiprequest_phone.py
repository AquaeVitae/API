# Generated by Django 4.2.7 on 2024-03-18 18:34

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("partnerships", "0010_alter_partnershiprequest_company_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partnershiprequest",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, null=True, region=None
            ),
        ),
    ]