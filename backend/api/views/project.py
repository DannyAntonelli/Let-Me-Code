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
                **ProjectSerializer(project).data,
                "file_ids": [file.id for file in project.files.all()],
                "creator_username": project.user.username,
                "shared_usernames": [
                    user.username for user in project.shared_users.all()
                ],
                "is_favorite": request.user in project.favorite_users.all(),
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
        public = request.data.get("public", False)
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


class SearchProjects(APIView):
    def get(self, request: Request) -> Response:
        query = request.query_params.get("query")

        if query is None:
            return Response(
                {"message": "Query is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        projects = (
            Project.objects.filter(
                name__icontains=query,
                shared_users__in=[request.user],
            )
            | Project.objects.filter(
                name__icontains=query,
                user=request.user,
            )
            | Project.objects.filter(
                name__icontains=query,
                is_public=True,
            )
        ).distinct()

        QUERY_LIMIT = 50
        return Response(
            {
                "projects": [
                    {
                        **ProjectSerializer(project).data,
                        "creator_username": project.user.username,
                        "is_favorite": request.user in project.favorite_users.all(),
                        "languages": list(
                            {file.language.lower() for file in project.files.all()}
                        ),
                    }
                    for project in projects[:QUERY_LIMIT]
                ]
            }
        )


class ToggleFavorite(APIView):
    permission_classes = [IsPublicOrCreatorOrShared]

    def post(self, request: Request, project_id: int) -> Response:
        favorite = request.data.get("favorite", False)
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(request, project)
        if favorite:
            project.favorite_users.add(request.user)
        else:
            project.favorite_users.remove(request.user)
        return Response(
            {
                "message": f"Project status changed successfully, favorite = {str(favorite).lower()}",
            }
        )


class GetFollowingProjects(APIView):
    def get(self, request: Request) -> Response:
        following_users = [profile.user for profile in request.user.following.all()]
        projects = (
            Project.objects.filter(
                user__in=following_users,
                is_public=True,
            )
            | Project.objects.filter(
                user__in=following_users,
                shared_users__in=[request.user],
            ).distinct()
        )

        return Response(
            {
                "projects": [
                    {
                        **ProjectSerializer(project).data,
                        "creator_username": project.user.username,
                        "is_favorite": request.user in project.favorite_users.all(),
                        "languages": list(
                            {file.language.lower() for file in project.files.all()}
                        ),
                    }
                    for project in projects
                ]
            }
        )


class GetFavoriteProjects(APIView):
    def get(self, request: Request) -> Response:
        projects = Project.objects.filter(favorite_users__in=[request.user])

        return Response(
            {
                "projects": [
                    {
                        **ProjectSerializer(project).data,
                        "creator_username": project.user.username,
                        "is_favorite": request.user in project.favorite_users.all(),
                        "languages": list(
                            {file.language.lower() for file in project.files.all()}
                        ),
                    }
                    for project in projects
                ]
            }
        )
