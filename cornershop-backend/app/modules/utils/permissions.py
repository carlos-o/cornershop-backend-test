from rest_framework.permissions import BasePermission
from django.core.exceptions import PermissionDenied
from app.modules.accounts.models import User


class OrderPermissions(BasePermission):
    """
        Verify if user to realize this request is admin or belong to staff member
    """
    message = "The access method is not allowed"

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user and request.user.is_staff
        elif request.method == 'POST':
            return request.user and request.user.groups.all().filter(name=User.USER_EMPLOYEE).exists()


def is_active_user(func):
    """
        Decorator function for services to test whether the user who uses
        the service is active
    """

    def decorator(*args, **kwargs):
        """
            if "user" not in kwargs:
            raise ValueError("A 'user' named argument must be provided")
        """
        user = kwargs['user']

        if user is None:
            raise ValueError("User can't be None")

        if user.is_active is False:
            raise PermissionDenied("Account blocked, contact the administrators.")

        return func(*args, **kwargs)

    return decorator
