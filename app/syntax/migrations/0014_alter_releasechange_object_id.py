# Generated by Django 4.0.4 on 2022-06-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syntax', '0013_releasechange_parent_release_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releasechange',
            name='object_id',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
