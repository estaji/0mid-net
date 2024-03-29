# Generated by Django 4.1 on 2023-01-05 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0012_resumeconfig_delete_configuration_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="resumeconfig",
            name="skills_style",
            field=models.CharField(
                choices=[("a", "accordion style"), ("t", "text style")],
                default="a",
                max_length=1,
                verbose_name="Skills section style",
            ),
        ),
    ]
