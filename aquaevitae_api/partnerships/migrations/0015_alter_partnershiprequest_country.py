# Generated by Django 4.2.7 on 2024-03-20 15:04

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):
    dependencies = [
        ("partnerships", "0014_rename_message_partnershiprequest_agent_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partnershiprequest",
            name="country",
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]