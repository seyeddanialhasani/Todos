# Generated by Django 4.2.4 on 2023-08-11 11:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name="tweets",
            name="title",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="tweets",
            name="text",
            field=models.CharField(max_length=256),
        ),
        migrations.AddField(
            model_name="tweets",
            name="author",
            field=models.ForeignKey(
                default=django.utils.timezone.now,
                on_delete=django.db.models.deletion.CASCADE,
                to="pages.author",
            ),
            preserve_default=False,
        ),
    ]
