from django.db import models

from core.models import BaseModel


class Workflow(BaseModel):
    model = models.ForeignKey('db.ModelSchema', on_delete=models.CASCADE, related_name='workflows')
    workflow_name = models.CharField(max_length=255)
    definition = models.JSONField(default=dict)

    def __str__(self):
        return self.workflow_name
