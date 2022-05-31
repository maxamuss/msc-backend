# Generated by Django 4.0.4 on 2022-05-31 11:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('syntax', '0002_syntaxdefinition_delete_syntax'),
    ]

    operations = [
        migrations.AddField(
            model_name='syntaxdefinition',
            name='object_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='syntaxdefinition',
            name='syntax_version',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='syntaxdefinition',
            name='syntax_type',
            field=models.CharField(choices=[('model', 'Model'), ('page', 'Page'), ('function', 'Function'), ('workflow', 'Workflow'), ('package', 'Package')], max_length=10),
        ),
    ]