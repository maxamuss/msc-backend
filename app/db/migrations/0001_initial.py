# Generated by Django 4.0.4 on 2022-06-14 11:50

import db.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldSchema',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=63)),
                ('class_name', models.TextField()),
                ('kwargs', db.models.FieldKwargsJSON(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='ModelSchema',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='modelschema',
            index=models.Index(fields=['name'], name='db_modelsch_name_980b8a_idx'),
        ),
        migrations.AddField(
            model_name='fieldschema',
            name='model_schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='db.modelschema'),
        ),
        migrations.AlterUniqueTogether(
            name='fieldschema',
            unique_together={('name', 'model_schema')},
        ),
    ]
