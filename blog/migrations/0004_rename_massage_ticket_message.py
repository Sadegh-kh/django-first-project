# Generated by Django 4.2.2 on 2023-07-01 08:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_ticket"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ticket",
            old_name="massage",
            new_name="message",
        ),
    ]
