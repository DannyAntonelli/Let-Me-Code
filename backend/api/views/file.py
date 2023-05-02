from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import File, Project
from ..permissions import (
    IsFileInEditableProject,
    IsFileInPermittedProject,
)
from ..serializers import FileSerializer


class GetFile(APIView):
    permission_classes = [IsFileInPermittedProject]

    def get(self, request: Request, file_id: int) -> Response:
        file = get_object_or_404(File, id=file_id)
        self.check_object_permissions(request, file)
        return Response({"file":FileSerializer(file).data})


class SyncFile(APIView):
    permission_classes = [IsFileInEditableProject]

    def post(self, request: Request, file_id: int) -> Response:
        content = request.data.get("content", "")
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
    permission_classes = [IsFileInEditableProject]

    def post(self, request: Request, project_id: int) -> Response:
        name = request.data.get("name")
        language = request.data.get("language")
        if not name or not language:
            return Response(
                {"message": "Name and language are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if name[0] != "/":
            name = "/" + name
        project = get_object_or_404(Project, id=project_id)
        file = File(name=name, language=language, content="", project=project)
        self.check_object_permissions(request, file)
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


class DeleteFile(APIView):
    permission_classes = [IsFileInEditableProject]

    def delete(self, request: Request, file_id: int) -> Response:
        file = get_object_or_404(File, id=file_id)
        self.check_object_permissions(request, file)
        file.delete()
        return Response(
            {
                "message": "File deleted successfully",
            }
        )
