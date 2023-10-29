from rest_framework import permissions


class IsOwnerOrAdminUser(permissions.BasePermission):
    """
    This custom permission allows only owner or admin to create and modify instances
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.user == request.user:
            return True
        return False
