from django.contrib import admin

from .models import File, Project, Profile


admin.site.register(File)
admin.site.register(Project)
admin.site.register(Profile)
