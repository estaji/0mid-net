# Generated by Django 4.0.4 on 2022-05-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0005_alter_jumbotron_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jumbotron",
            name="picture",
            field=models.ImageField(
                upload_to="jumbotron_picture/", verbose_name="Picture/Avatar"
            ),
        ),
    ]
