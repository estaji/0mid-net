# Generated by Django 4.1 on 2022-10-20 08:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("scan", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="tried",
        ),
    ]
