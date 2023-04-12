from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import File, Project
from .serializers import UserSerializer, FileSerializer, ProjectSerializer
from .permissions import IsCreatorOrShared, IsPublicOrCreatorOrShared


class TestIsAuth(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        return Response({"message": "You are authenticated"})


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
        project_ids = [
            project.id
            for project in user.projects.all()
            if IsPublicOrCreatorOrShared.has_object_permission(
                self, request, None, project
            )
        ]
        shared_project_ids = [
            project.id
            for project in user.shared_projects.all()
            if IsPublicOrCreatorOrShared.has_object_permission(
                self, request, None, project
            )
        ]

        return Response(
            {
                "user": UserSerializer(user).data,
                "project_ids": project_ids,
                "shared_project_ids": shared_project_ids,
            }
        )


class GetProject(APIView):
    permission_classes = [IsPublicOrCreatorOrShared]

    def get(self, request: HttpRequest, project_id: int):
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(request, project)
        return Response(ProjectSerializer(project).data)
