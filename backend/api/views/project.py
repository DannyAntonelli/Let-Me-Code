from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Project
from ..permissions import IsCreator, IsPublicOrCreatorOrShared
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
                "creator_username": project.user.username,
                "shared_usernames": [
                    user.username for user in project.shared_users.all()
                ],
            }
        )


class CreateProject(APIView):
    def post(self, request: Request) -> Response:
        name = request.data.get("name")
        description = request.data.get("description", "")
        is_public = request.data.get("is_public", "false").lower() == "true"

        if not name:
            return Response(
                {"message": "Name is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        project = Project(
            name=name,
            description=description,
            is_public=is_public,
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
    permission_classes = [IsCreator]

    def post(self, request: Request, project_id: int) -> Response:
        username = request.data.get("username")
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(request, project)
        user = User.objects.get(username=username)
        project.shared_users.add(user)
        return Response(
            {
                "message": "Project shared successfully",
            }
        )


class MakePublic(APIView):
    permission_classes = [IsCreator]

    def post(self, request: Request, project_id: int) -> Response:
        public = request.data.get("public").lower() == "true"
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(request, project)
        project.is_public = public
        project.save()
        return Response(
            {
                "message": f"Project status changed successfully, public = {str(public).lower()}",
            }
        )


class DeleteProject(APIView):
    permission_classes = [IsCreator]

    def delete(self, request: Request, project_id: int) -> Response:
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(request, project)
        project.delete()
        return Response(
            {
                "message": "Project deleted successfully",
            }
        )
