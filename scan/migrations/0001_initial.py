# Generated by Django 4.1 on 2022-10-10 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Node",
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
                    "node_type",
                    models.CharField(
                        choices=[("c", "Child"), ("p", "Parent")],
                        max_length=1,
                        verbose_name="Node Type",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Location"
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        default="https://#",
                        max_length=50,
                        unique=True,
                        verbose_name="URL",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Is active"),
                ),
                (
                    "token",
                    models.CharField(blank=True, max_length=40, verbose_name="Token"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Job id"
                    ),
                ),
                (
                    "add_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="Add time"),
                ),
                ("start_time", models.DateTimeField(verbose_name="Start time")),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="Last update"),
                ),
                (
                    "command",
                    models.CharField(
                        choices=[("pi", "ping instantly"), ("p", "ping")],
                        max_length=2,
                        verbose_name="Command type",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("n", "none"),
                            ("r", "running"),
                            ("s", "success"),
                            ("f", "failed"),
                        ],
                        default="n",
                        max_length=1,
                        verbose_name="Status",
                    ),
                ),
                ("tried", models.IntegerField(default=0, verbose_name="Try")),
                ("uuid", models.UUIDField(verbose_name="UUID")),
                ("url", models.URLField(max_length=300, verbose_name="URL")),
                (
                    "result",
                    models.CharField(blank=True, max_length=100, verbose_name="Result"),
                ),
                (
                    "node",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scan.node",
                        verbose_name="Node",
                    ),
                ),
            ],
        ),
    ]
