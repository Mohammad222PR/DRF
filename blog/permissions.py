from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == SAFE_METHODS:
            return True
        return obj.user == request.user


