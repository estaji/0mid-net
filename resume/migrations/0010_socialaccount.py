# Generated by Django 4.0.4 on 2022-04-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_jumbotron'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin', models.URLField(blank=True, default='#')),
                ('github', models.URLField(blank=True, default='#')),
                ('stackexchange', models.URLField(blank=True, default='#', max_length=254)),
                ('instagram', models.URLField(blank=True, default='#')),
                ('twitter', models.URLField(blank=True, default='#')),
            ],
        ),
    ]
