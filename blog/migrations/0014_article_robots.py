# Generated by Django 4.0.4 on 2022-06-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_article_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='robots',
            field=models.CharField(blank=True, max_length=60, verbose_name='Meta robots tag'),
        ),
    ]