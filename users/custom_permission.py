from rest_framework.permissions import BasePermission


class HasAdminRole(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin' or request.user.is_superuser:
            return True
        return False
