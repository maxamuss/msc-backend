# Generated by Django 4.0.4 on 2022-05-31 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syntax', '0008_remove_releasechange_release_version_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='current_release',
            field=models.BooleanField(default=False),
        ),
    ]