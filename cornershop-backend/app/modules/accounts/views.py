from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import (
    permissions,
    status
)
from rest_framework.response import Response
from app.modules.accounts import (
    services as accounts_services,
    serializers as accounts_serializers,
)
from app.modules.utils.response import ResponseDetail
from django.core.exceptions import PermissionDenied
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    logger.info("Make authentication to API")
    try:
        user = accounts_services.login(request.data)
    except ValueError as e:
        logger.error("ValueError: %s" % str(e), exc_info=True)
        return Response(ResponseDetail().errors_detail(code=400, message="ValueError", error=str(e)),
                        status=status.HTTP_400_BAD_REQUEST)
    except PermissionDenied as e:
        logger.error("PermissionError: %s" % str(e), exc_info=True)
        return Response(ResponseDetail().errors_detail(code=401, message="PermissionError", error=str(e)),
                        status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        logger.error("Exception: INTERNAL SERVER ERROR %s" % str(e), exc_info=True)
        return Response(ResponseDetail().errors_detail(error={"error": str(e)}),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = accounts_serializers.UserSerializers(user, many=False).data
    token, created = Token.objects.get_or_create(user=user)
    serializer['token'] = token.key
    return Response(ResponseDetail().success_detail(data=serializer), status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny, permissions.IsAuthenticated])
def logout_view(request):
    """
        Deletes the user's token in the system.
    """
    logger.info("Logout from the API")
    try:
        accounts_services.logout(user=request.user)
    except ValueError as e:
        logger.error("ValueError: %s" % str(e), exc_info=True)
        return Response(ResponseDetail().errors_detail(code=400, message="ValueError", error=str(e)),
                        status=status.HTTP_400_BAD_REQUEST)
    except PermissionDenied as e:
        logger.error("PermissionError: %s" % str(e), exc_info=True)
        return Response(ResponseDetail().errors_detail(code=401, message="Permission Denied", error=str(e)),
                        status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        logger.error("Exception: INTERNAL SERVER ERROR %s" % str(e), exc_info=True)
        return Response(ResponseDetail().errors_detail(error={"error": str(e)}),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(ResponseDetail().success_detail(), status=status.HTTP_200_OK)
