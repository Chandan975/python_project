from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.role == 'admin':
            return True
        if view.action == 'list':
            return True
        return False
