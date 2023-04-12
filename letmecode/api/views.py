from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import File, Project
from .serializers import UserSerializer, FileSerializer, ProjectSerializer


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
    def get(self, request: HttpRequest, username: int):
        user = User.objects.get(username=username)
        project_ids = [project.id for project in user.projects.all()]
        shared_project_ids = [project.id for project in user.shared_projects.all()]

        return Response(
            {
                "user": UserSerializer(user).data,
                "project_ids": project_ids,
                "shared_project_ids": shared_project_ids,
            }
        )
