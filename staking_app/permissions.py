from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthentificatedReadOnly(permissions.BasePermission):
    """
    Custom permission to allow admin to have full access, authenticated users to have read-only access,
    and to limit deleting capability to the owner.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        return True  # Allow any authenticated user to create, update, or delete

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access.
    """

    def has_permission(self, request, view):
        # Check if the user is an admin
        return request.user and request.user.is_staff


class IsAuthenticatedReadOnly(permissions.BasePermission):
    """
    Custom permission to allow read-only access for authenticated users.
    """

    def has_permission(self, request, view):
        # Check if the request is a read-only request and if the user is authenticated
        return request.method in permissions.SAFE_METHODS and request.user and request.user.is_authenticated

