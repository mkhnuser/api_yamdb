from rest_framework import permissions


class CustomRolePermissions(permissions.BasePermission):

    def has_permission(self, request, view):

        role_map = {
            'admin': ['POST', 'GET', 'DELETE'],
            'user': ['GET'],
            'moderator': ['GET'],
        }

        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        if user.is_superuser == 1:
            return True
        if user.is_anonymous:
            return False
        user_methods = role_map.get(user.role)
        if user_methods and request.method in user_methods:
            return True
        return False
