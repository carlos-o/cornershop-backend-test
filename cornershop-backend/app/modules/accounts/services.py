from app.modules.accounts.models import User
from django.db.models import Q
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from datetime import datetime
from app.modules.utils.permissions import is_active_user
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


def login(data: dict) -> dict:
    """
        Get access to application.
        Raise exception if user or password are incorrect or user does not exist.

        :param data: username and password of user.
        :type data: dict.
        :return: user.
        :raises: ValueError, PermissionDenied.
    """
    username = data.get("username", None)
    password = data.get("password", None)
    logger.debug("Verify: is user data is not empty")
    if username is None or not username:
        logger.error("OPEN:Error username is empty", exc_info=True)
        raise ValueError("The username cannot be empty")
    if password is None or not password:
        logger.error("OPEN:Error password is empty", exc_info=True)
        raise ValueError("The password cannot be empty")
    logger.debug("Verify is user data if correct to provide access")
    try:
        # Obtain user from database if exist
        user = User.objects.get(Q(username=username) | Q(email=username.lower()))
    except Exception as e:
        logger.error("OPEN:Error in petition to login user %s" % str(e), exc_info=True)
        raise ValueError("The username or password is incorrect")
    # Verify is user is active
    if not user.is_active:
        logger.error("OPEN:Error %s accounts is inactive" % user.username, exc_info=True)
        raise PermissionDenied("Account blocked, contact the administrators.")
    # Verify if password match
    if not user.check_password(password):
        logger.error("OPEN:Error %s password doesnot match " % user.username, exc_info=True)
        raise ValueError("The username or password is incorrect")
    logger.debug('OPEN: %s login correctly into API' % user.username)
    user = authenticate(username=user.username, password=password)
    return user


@is_active_user
def logout(user: User) -> bool:
    """
        Remove token access to user into massone-api.
        Raises exception if user is inactive.

        :param user: User into app
        :type: Model User.
        :return: User.
        :raises: ValueError.
    """
    logger.debug("add date to user when he has logout")
    user.last_login = datetime.now()
    user.save()
    logger.debug("remove token access to %s" % user.username)
    user.auth_token.delete()
    logger.debug("OPEN: %s has been logout to app correctly" % user.username)
    return True
