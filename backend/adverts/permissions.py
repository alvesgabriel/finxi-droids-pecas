from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to adverts action only allows to advertiser
    """

    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return True
        return obj.user == request.user
