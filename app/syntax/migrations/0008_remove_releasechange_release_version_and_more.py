# Generated by Django 4.0.4 on 2022-05-31 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syntax', '0007_alter_release_release_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='releasechange',
            name='release_version',
        ),
        migrations.AddField(
            model_name='release',
            name='functions',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='release',
            name='modelschemas',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='release',
            name='packages',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='release',
            name='pages',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='release',
            name='workflows',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='releasechange',
            name='change_type',
            field=models.CharField(choices=[('create', 'Create'), ('update', 'Update'), ('delete', 'Delete')], default='create', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='releasechange',
            name='model_type',
            field=models.CharField(default='modelschema', max_length=30),
            preserve_default=False,
        ),
    ]
