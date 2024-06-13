from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = "Вы не состоите в группе 'moderator'"

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
