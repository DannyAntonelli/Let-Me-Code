from django.db import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import File, Project
from .serializers import UserSerializer, FileSerializer, ProjectSerializer
from .permissions import (
    IsPublicOrCreatorOrShared,
    IsFileInPermittedProject,
)


class Register(APIView):
    def post(self, request: Request) -> Response:
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
    def get(self, request: Request, username: str) -> Response:
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

    def get(self, request: Request, project_id: int) -> Response:
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

    def get(self, request: Request, file_id: int) -> Response:
        file = get_object_or_404(File, id=file_id)
        self.check_object_permissions(request, file)
        return Response(FileSerializer(file).data)


class CreateProject(APIView):
    def post(self, request: Request) -> Response:
        name = request.data.get("name")
        description = request.data.get("description")
        is_public = request.data.get("is_public")
        if not request.user.is_authenticated:
            return Response(
                {"message": "You must be logged in to create a project"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not name:
            return Response(
                {"message": "Name is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        project = Project(
            name=name,
            description=description if description else "",
            is_public=is_public if is_public else False,
            user=request.user,
        )
        try:
            project.save()
        except IntegrityError:
            return Response(
                {"message": "Project with this name already exists for this user"},
                status=status.HTTP_409_CONFLICT,
            )

        return Response(
            {
                "message": "Project created successfully",
                "project_id": project.id,
            }
        )


class CreateFile(APIView):
    def post(self, request: Request, project_id: int) -> Response:
        name = request.data.get("name")
        language = request.data.get("language")
        if not request.user.is_authenticated:
            return Response(
                {"message": "You must be logged in to create a file"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if not name or not language:
            return Response(
                {"message": "Name and language are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        project = get_object_or_404(Project, id=project_id)
        if not IsPublicOrCreatorOrShared.has_object_permission(
            self, request, None, project
        ):
            return Response(
                {
                    "message": "You do not have permission to create a file in this project"
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        file = File(name=name, language=language, content="", project=project)
        try:
            file.save()
        except IntegrityError:
            return Response(
                {"message": "File with this name already exists in this project"},
                status=status.HTTP_409_CONFLICT,
            )
        return Response(
            {
                "message": "File created successfully",
                "file_id": file.id,
            }
        )


class SyncFile(APIView):
    def post(self, request: Request, file_id: int) -> Response:
        content = request.data.get("content")
        file = get_object_or_404(File, id=file_id)
        self.check_object_permissions(request, file)
        file.content = content
        file.save()
        return Response(
            {
                "message": "File synced successfully",
            }
        )


class ShareProject(APIView):
    def post(self, request: Request, project_id: int) -> Response:
        username = request.data.get("username")
        if not request.user.is_authenticated:
            return Response(
                {"message": "You must be logged in to share a project"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        project = get_object_or_404(Project, id=project_id)
        if not IsPublicOrCreatorOrShared.has_object_permission(
            self, request, None, project
        ):
            return Response(
                {"message": "You do not have permission to share this project"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        user = get_object_or_404(User, username=username)
        project.shared_users.add(user)
        return Response(
            {
                "message": "Project shared successfully",
            }
        )


class MakePublic(APIView):
    def post(self, request: Request, project_id: int) -> Response:
        public = request.data.get("public")
        if not request.user.is_authenticated:
            return Response(
                {"message": "You must be logged in to make a project public"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        project = get_object_or_404(Project, id=project_id)
        if not IsPublicOrCreatorOrShared.has_object_permission(
            self, request, None, project
        ):
            return Response(
                {"message": "You do not have permission to make this project public"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        project.is_public = public
        project.save()
        return Response(
            {
                "message": f"Project status changed successfully, public= {public}",
            }
        )
