from rest_framework.permissions import BasePermission


class HasAdminRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin or request.user.is_superuser
