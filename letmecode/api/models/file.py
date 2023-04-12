from django.db import models

from ..models import Project


class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    language = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="files")

    class Meta:
        unique_together = ["name", "project"]
