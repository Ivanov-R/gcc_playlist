# Generated by Django 4.1.7 on 2023-02-27 14:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PlaylistsSongs",
            new_name="PlaylistsSong",
        ),
    ]