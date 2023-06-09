# Generated by Django 4.2 on 2023-04-13 09:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0003_remove_project_files_file_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="project",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name="file",
            unique_together={("name", "project")},
        ),
        migrations.AlterUniqueTogether(
            name="project",
            unique_together={("name", "user")},
        ),
    ]
