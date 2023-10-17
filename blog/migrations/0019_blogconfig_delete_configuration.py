# Generated by Django 4.1 on 2022-10-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0018_tag_robots"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "copyr",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Copyright message in footer",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "linkedin",
                    models.URLField(
                        blank=True, default="#", verbose_name="Linkedin Account"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="Blog Name",
                        max_length=50,
                        verbose_name="Title in menu bar",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        default="Blog Title",
                        max_length=70,
                        verbose_name="Title in main page",
                    ),
                ),
                (
                    "subtitle",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Sub-title in main page",
                    ),
                ),
                (
                    "meta_author",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Meta author tag"
                    ),
                ),
                (
                    "meta_description",
                    models.CharField(
                        blank=True, max_length=160, verbose_name="Meta description tag"
                    ),
                ),
                (
                    "keywords",
                    models.CharField(
                        blank=True, max_length=160, verbose_name="Meta keywords tag"
                    ),
                ),
                (
                    "robots",
                    models.CharField(
                        blank=True, max_length=60, verbose_name="Meta robots tag"
                    ),
                ),
                (
                    "twitter_user",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        verbose_name="Twitter username for Twitter site tag",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Configuration",
        ),
    ]
