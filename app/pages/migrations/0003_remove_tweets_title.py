# Generated by Django 4.2.4 on 2023-08-11 11:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0002_author_tweets_title_alter_tweets_text_tweets_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tweets",
            name="title",
        ),
    ]