from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import View

from .models import File, Project


class IsCreator(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request: Request, view, obj: Project) -> bool:
        return obj.user == request.user


class IsCreatorOrShared(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request: Request, view, obj: Project) -> bool:
        return (
            IsCreator.has_object_permission(self, request, view, obj)
            or request.user in obj.shared_users.all()
        )


class IsPublicOrCreatorOrShared(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request: Request, view, obj: Project) -> bool:
        return obj.is_public or IsCreatorOrShared.has_object_permission(
            self, request, view, obj
        )


class IsFileInEditableProject(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request: Request, view, obj: File) -> bool:
        return IsCreatorOrShared.has_object_permission(self, request, view, obj.project)


class IsFileInPermittedProject(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request: Request, view, obj: File) -> bool:
        return IsPublicOrCreatorOrShared.has_object_permission(
            self, request, view, obj.project
        )
