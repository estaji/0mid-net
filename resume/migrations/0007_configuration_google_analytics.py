# Generated by Django 4.0.4 on 2022-05-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_alter_jumbotron_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='google_analytics',
            field=models.TextField(blank=True, verbose_name='Google analytics global site tag'),
        ),
    ]