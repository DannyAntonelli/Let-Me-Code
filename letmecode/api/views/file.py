from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import File, Project
from ..permissions import (
    IsFileInPermittedProject,
    IsPublicOrCreatorOrShared,
)
from ..serializers import FileSerializer


class GetFile(APIView):
    permission_classes = [IsFileInPermittedProject]

    def get(self, request: Request, file_id: int) -> Response:
        file = get_object_or_404(File, id=file_id)
        self.check_object_permissions(request, file)
        return Response(FileSerializer(file).data)


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
