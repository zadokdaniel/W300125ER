from rest_framework import permissions
from rest_framework.request import Request


class isAdminOrModerator(permissions.BasePermission):
    """
    Allows access only to admin user or moderators
    """

    def has_permission(self, request: Request, view):
        is_admin = bool(request.user and
                        request.user.is_staff and request.user.is_superuser)

        if is_admin:
            return True

        in_group = request.user.groups.filter(name='moderator').exists()

        return in_group


class IsAllowedOrOwner(permissions.DjangoModelPermissions):

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS and super().has_object_permission(request, view, obj)):
            return True

        return obj.author == request.user or request.user.is_superuser
