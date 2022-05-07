# Generated by Django 4.0.4 on 2022-05-07 11:46

import db.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('class_name', models.TextField()),
                ('kwargs', db.models.FieldKwargsJSON(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='ModelSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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