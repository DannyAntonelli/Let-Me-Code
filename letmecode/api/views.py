from django.db import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import File, Project
from .serializers import UserSerializer, FileSerializer, ProjectSerializer
from .permissions import (
    IsPublicOrCreatorOrShared,
    IsFileInPermittedProject,
)


class Register(APIView):
    def post(self, request: HttpRequest):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"message": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            return Response({"message": "User created successfully"})
        except IntegrityError:
            return Response(
                {"message": "Username already taken"},
                status=status.HTTP_409_CONFLICT,
            )


class GetUser(APIView):
    def get(self, request: HttpRequest, username: str):
        user = get_object_or_404(User, username=username)
        return Response(
            {
                "user": UserSerializer(user).data,
                "project_ids": [
                    project.id
                    for project in user.projects.all()
                    if IsPublicOrCreatorOrShared.has_object_permission(
                        self, request, None, project
                    )
                ],
                "shared_project_ids": [
                    project.id
                    for project in user.shared_projects.all()
                    if IsPublicOrCreatorOrShared.has_object_permission(
                        self, request, None, project
                    )
                ],
            }
        )


class GetProject(APIView):
    permission_classes = [IsPublicOrCreatorOrShared]

    def get(self, request: HttpRequest, project_id: int):
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(request, project)
        return Response(
            {
                "project": ProjectSerializer(project).data,
                "file_ids": [file.id for file in project.files.all()],
            }
        )


class GetFile(APIView):
    permission_classes = [IsFileInPermittedProject]

    def get(self, request: HttpRequest, file_id: int):
        file = get_object_or_404(File, id=file_id)
        self.check_object_permissions(request, file)
        return Response(FileSerializer(file).data)
