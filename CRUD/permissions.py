from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Разрешение, позволяющее редактировать или удалять объект
    только его автору.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
