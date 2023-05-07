from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import IsPublicOrCreatorOrShared
from ..serializers import UserSerializer


class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        username = request.data.get("username")
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"message": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
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
                "favorite_project_ids": [
                    project.id
                    for project in user.favorite_projects.all()
                    if IsPublicOrCreatorOrShared.has_object_permission(
                        self, request, None, project
                    )
                ],
            }
        )


class SearchUsers(APIView):
    def get(self, request: Request) -> Response:
        query = request.query_params.get("query")

        if query is None:
            return Response(
                {"message": "Query is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users = User.objects.filter(username__icontains=query)
        QUERY_LIMIT = 50

        return Response(
            {
                "users": [
                    {
                        **UserSerializer(user).data,
                        "number_of_public_projects": user.projects.filter(
                            is_public=True
                        ).count(),
                        "number_of_shared_public_projects": user.shared_projects.filter(
                            is_public=True
                        ).count(),
                    }
                    for user in users[:QUERY_LIMIT]
                ]
            }
        )
