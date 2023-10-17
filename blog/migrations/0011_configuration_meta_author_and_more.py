# Generated by Django 4.0.4 on 2022-06-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_article_meta_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="configuration",
            name="meta_author",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Meta author tag"
            ),
        ),
        migrations.AddField(
            model_name="configuration",
            name="meta_description",
            field=models.CharField(
                blank=True, max_length=160, verbose_name="Meta description tag"
            ),
        ),
    ]
