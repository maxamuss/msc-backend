# Generated by Django 4.0.4 on 2022-06-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syntax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releasesyntax',
            name='syntax_json',
            field=models.JSONField(),
        ),
    ]