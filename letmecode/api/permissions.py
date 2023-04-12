from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import View

from .models import File, Project


class IsCreatorOrShared(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request: Request, view, obj: Project) -> bool:
        return obj.user == request.user or request.user in obj.shared_users.all()


class IsPublicOrCreatorOrShared(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request: Request, view, obj: Project) -> bool:
        return (
            obj.is_public
            or obj.user == request.user
            or request.user in obj.shared_users.all()
        )


class IsFileInPermittedProject(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request: Request, view, obj: File) -> bool:
        return IsPublicOrCreatorOrShared.has_object_permission(
            self, request, view, obj.project
        )
