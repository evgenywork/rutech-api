from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user ==request.user


class IsGuest(BasePermission):
    """
    Allows access only to guest users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_guest)


class IsUser(BasePermission):
    """
    Allows access only to user users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_user)


class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)