from rest_framework import permissions


ROLE_MAP = {
    'admin': ('POST', 'GET', 'DELETE',),
    'user': ('GET',),
    'moderator': ('GET',),
}


class CustomRolePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_anonymous:
            return False
        if request.user.is_superuser:
            return True
        allowed_user_methods = ROLE_MAP.get(request.user.role)
        if allowed_user_methods and request.method in allowed_user_methods:
            return True
        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_anonymous:
            return False
        if (request.user.is_superuser
            or request.user.is_admin 
            or request.user.is_moderator 
            or request.user == obj.author):
                return True
        return False
