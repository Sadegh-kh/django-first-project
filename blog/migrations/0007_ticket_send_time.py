# Generated by Django 4.2.2 on 2023-07-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_post_reading_time_alter_comment_active_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="send_time",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="تاریخ ارسال"
            ),
        ),
    ]