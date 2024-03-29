# Generated by Django 4.0.4 on 2022-05-27 05:36

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("title", models.CharField(max_length=200, verbose_name="Title")),
                (
                    "slug",
                    models.SlugField(
                        max_length=150, unique=True, verbose_name="Slug/URL"
                    ),
                ),
                ("position", models.IntegerField(unique=True, verbose_name="Position")),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=250, verbose_name="Title")),
                (
                    "slug",
                    models.SlugField(
                        max_length=150, unique=True, verbose_name="Slug/URL"
                    ),
                ),
                ("content", models.TextField(verbose_name="Content")),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        upload_to="blog_thumbnail/",
                        verbose_name="Thumbnail",
                    ),
                ),
                (
                    "publish_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Published on"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created on"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated on"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("d", "Draft"), ("p", "Published")],
                        max_length=1,
                        verbose_name="Status",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[("en", "English"), ("fa", "Persian")],
                        max_length=2,
                        verbose_name="Language",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="articles",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author",
                    ),
                ),
                (
                    "tag",
                    models.ManyToManyField(
                        related_name="articles", to="blog.tag", verbose_name="Tag"
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
                "ordering": ["-publish_date"],
            },
        ),
    ]
