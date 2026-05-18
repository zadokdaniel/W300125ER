from rest_framework import permissions
from rest_framework.request import Request


class isAdminOrModerator(permissions.BasePermission):
    """
    Allows access only to admin user or moderators
    """

    def has_permission(self, request: Request, view):
        is_admin = bool(request.user and (
            request.user.is_staff or request.user.is_superuser))

        if is_admin:
            return True

        in_group = request.user.groups.filter(name='moderator').exists()

        return in_group
