# Generated by Django 4.2.4 on 2023-09-10 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("twitter_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tweet", old_name="nick", new_name="nickname",
        ),
    ]
