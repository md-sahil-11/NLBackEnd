from rest_framework import permissions

class AppActionBasedPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user is None:
            return False
        if not user.is_superuser and view.action in ['list', 'retrieve']:
            return user.is_authenticated 
        return user.is_superuser

