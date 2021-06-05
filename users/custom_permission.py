from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'admin'
