from rest_framework import permissions


ROLE_MAP = {
    'admin': ('POST', 'GET', 'DELETE'),
    'user': ('GET'),
    'moderator': ('GET'),
}



class CustomRolePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user

        if user.is_superuser:
            return True
        if user.is_anonymous:
            return False
        user_methods = ROLE_MAP.get(user.role)
        if user_methods and request.method in user_methods:
            return True
        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_anonymous:
            return False
        if (request.user.role in ('moderator', 'admin')
                or request.user == obj.author):
            return True
        return False
