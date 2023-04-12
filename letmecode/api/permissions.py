from rest_framework import permissions


class IsCreatorOrShared(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user in obj.shared_users.all()


class IsPublicOrCreatorOrShared(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            obj.is_public
            or obj.user == request.user
            or request.user in obj.shared_users.all()
        )
