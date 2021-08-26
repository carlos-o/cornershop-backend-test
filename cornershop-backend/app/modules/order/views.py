from rest_framework.generics import ListCreateAPIView
from rest_framework import (
	permissions,
	status
)
from app.modules.utils.response import ResponseDetail
from app.modules.utils.permissions import OrderPermissions
from rest_framework.response import Response
from .serializers import OrderSerializers
from .services import create_order
from app.modules.utils.pagination import CustomPagination
from .models import Order
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


class OrderListCreateView(ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializers
	permission_classes = [permissions.IsAuthenticated, OrderPermissions]

	def list(self, request, *args, **kwargs):
		"""
			only admin user has permission to call this method
		"""
		logger.info("get the list of all order")
		queryset = self.get_queryset()
		paginator = CustomPagination()
		context = paginator.paginate_queryset(queryset, request)
		serializer = self.get_serializer(context, many=True).data
		return paginator.get_paginated_response(serializer)

	def create(self, request, *args, **kwargs):
		logger.info("place an order from the menu")
		try:
			order = create_order(data=request.data, user=request.user)
		except ValueError as e:
			logger.error(f"ValueError: {e}", exc_info=True)
			return Response(
				ResponseDetail().errors_detail(code=400, message="ValueError", error=str(e)),
				status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			logger.error(f"Exception: INTERNAL SERVER ERROR {e}", exc_info=True)
			return Response(
				ResponseDetail().errors_detail(error={"error": str(e)}),
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = self.get_serializer(order, many=False).data
		return Response(
			ResponseDetail().success_detail(code=201, data=serializer, message="order has been created successfully"),
			status=status.HTTP_201_CREATED)
