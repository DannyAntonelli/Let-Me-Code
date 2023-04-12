from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    shared_users = models.ManyToManyField(
        User, blank=True, related_name="shared_projects"
    )

    class Meta:
        unique_together = ["name", "user"]
