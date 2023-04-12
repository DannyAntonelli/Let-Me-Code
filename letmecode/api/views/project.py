from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Project
from ..permissions import IsPublicOrCreatorOrShared
from ..serializers import ProjectSerializer


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
