# Generated by Django 3.2.4 on 2021-08-06 02:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0080_alter_shelfbook_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_active_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
