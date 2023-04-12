from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    shared_users = models.ManyToManyField(
        User, blank=True, related_name="shared_projects"
    )


class File(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    language = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="files")
