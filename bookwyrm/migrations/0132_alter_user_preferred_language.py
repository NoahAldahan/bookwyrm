# Generated by Django 3.2.10 on 2022-02-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0131_merge_20220125_1644"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="preferred_language",
            field=models.CharField(
                blank=True,
                choices=[
                    ("en-us", "English"),
                    ("de-de", "Deutsch (German)"),
                    ("es-es", "Español (Spanish)"),
                    ("gl-es", "Galego (Galician)"),
                    ("it-it", "Italiano (Italian)"),
                    ("fr-fr", "Français (French)"),
                    ("lt-lt", "Lietuvių (Lithuanian)"),
                    ("no-no", "Norsk (Norwegian)"),
                    ("pt-br", "Português do Brasil (Brazilian Portuguese)"),
                    ("pt-pt", "Português Europeu (European Portuguese)"),
                    ("sv-se", "Svenska (Swedish)"),
                    ("zh-hans", "简体中文 (Simplified Chinese)"),
                    ("zh-hant", "繁體中文 (Traditional Chinese)"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]