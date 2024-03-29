# Generated by Django 4.1 on 2022-10-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scan", "0003_scanconfig"),
    ]

    operations = [
        migrations.AddField(
            model_name="scanconfig",
            name="author",
            field=models.CharField(
                blank=True, max_length=160, verbose_name="Meta author tag"
            ),
        ),
        migrations.AddField(
            model_name="scanconfig",
            name="robots",
            field=models.CharField(
                blank=True, max_length=160, verbose_name="Meta robots tag"
            ),
        ),
        migrations.AddField(
            model_name="scanconfig",
            name="twitter_user",
            field=models.CharField(
                blank=True,
                max_length=50,
                verbose_name="Twitter username for Twitter site tag",
            ),
        ),
    ]
