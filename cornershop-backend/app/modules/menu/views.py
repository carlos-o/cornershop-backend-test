from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import (
	permissions,
	status
)
from rest_framework.response import Response
from app.modules.utils.response import ResponseDetail
from app.modules.utils.exceptions import NotFound
from app.modules.utils.pagination import CustomPagination
from app.modules.menu import (
	services as menu_services,
	serializers as menu_serializers,
	tasks as menu_tasks,
	models as menu_models
)
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


class MenuViewSet(ModelViewSet):
	permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
	serializer_class = menu_serializers.MenuSerializers
	queryset = menu_models.Menu.objects.all().order_by('-start_date')

	def get_queryset(self):
		queryset = menu_models.MenuUser.objects.select_related('menu').filter(user__id=self.request.user.id)
		return queryset

	def list(self, request, *args, **kwargs):
		logger.info("list with all menu create for specific user")
		paginator = CustomPagination()
		queryset = menu_models.Menu.objects.prefetch_related('menu_user').\
			filter(menu_user__user_id=self.request.user.id).order_by('-created_at')
		context = paginator.paginate_queryset(queryset, request)
		serializer = self.get_serializer(context, many=True).data
		return paginator.get_paginated_response(serializer)

	def retrieve(self, request, *args, **kwargs):
		logger.info("get specific menu")
		instance = self.get_object()
		serializer = self.get_serializer(instance.menu)
		return Response(ResponseDetail().success_detail(data=serializer.data))

	def create(self, request, *args, **kwargs):
		logger.info("Create a new menu")
		try:
			menu = menu_services.create_menu(data=request.data, user=request.user)
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
		serializer = self.get_serializer(menu, many=False).data
		return Response(
			ResponseDetail().success_detail(code=201, data=serializer, message="menu has been created successfully"),
			status=status.HTTP_201_CREATED)

	def update(self, request, *args, **kwargs):
		logger.info("update a specific menu")
		instance = self.get_object()
		try:
			menu = menu_services.update_menu(data=request.data, menu_user=instance, user=request.user)
		except ValueError as e:
			return Response(
				ResponseDetail().errors_detail(code=400, message="ValueError", error=str(e)),
				status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			logger.error("Exception: INTERNAL SERVER ERROR %s" % str(e), exc_info=True)
			return Response(
				ResponseDetail().errors_detail(error={"error": str(e)}),
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = self.get_serializer(menu, many=False).data
		return Response(
			ResponseDetail().success_detail(data=serializer, message="menu has been updated successfully"),
			status=status.HTTP_200_OK)

	def destroy(self, request, *args, **kwargs):
		logger.info("The destroy method does nothing")
		message = 'Delete function is not offered in this path'
		return Response(
			ResponseDetail().errors_detail(code=403, message=message), status=status.HTTP_403_FORBIDDEN)

	@action(
		methods=['POST'], url_path='option', detail=True,
		permission_classes=(permissions.IsAuthenticated, permissions.IsAdminUser)
	)
	def create_option(self, request, pk=None):
		logger.info("create a option to specific menu")
		instance = self.get_object()
		try:
			option = menu_services.create_option_menu(data=request.data, user=request.user, menu=instance.menu)
		except ValueError as e:
			logger.error(f"ValueError: {e}", exc_info=True)
			return Response(
				ResponseDetail().errors_detail(code=400, message="ValueError", error=str(e)),
				status=status.HTTP_400_BAD_REQUEST)
		except NotFound as e:
			logger.error(f"NotFound: {e}", exc_info=True)
			return Response(
				ResponseDetail().not_found_detail(message=str(e)), status=status.HTTP_404_NOT_FOUND)
		except Exception as e:
			logger.error(f"Exception: INTERNAL SERVER ERROR {e}", exc_info=True)
			return Response(
				ResponseDetail().errors_detail(error={"error": str(e)}),
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = menu_serializers.OptionSerializers(option, many=False).data
		return Response(
			ResponseDetail().success_detail(code=201, data=serializer, message="options has been added successfully"),
			status=status.HTTP_201_CREATED)

	@action(
		methods=['PUT'], url_path='option/(?P<option_id>[0-9]+)', detail=True,
		permission_classes=(permissions.IsAuthenticated, permissions.IsAdminUser)
	)
	def update_option(self, request, pk=None, option_id=None):
		logger.info("update a option to specific menu")
		instance = self.get_object()
		logger.info("update specific option")
		try:
			option = menu_services.update_option_menu(
				data=request.data, user=request.user, menu=instance.menu, option_id=option_id)
		except ValueError as e:
			logger.error(f"ValueError: {e}", exc_info=True)
			return Response(
				ResponseDetail().errors_detail(code=400, message="ValueError", error=str(e)),
				status=status.HTTP_400_BAD_REQUEST)
		except NotFound as e:
			logger.error(f"NotFound: {e}", exc_info=True)
			return Response(
				ResponseDetail().not_found_detail(message=str(e)), status=status.HTTP_404_NOT_FOUND)
		except Exception as e:
			logger.error(f"Exception: INTERNAL SERVER ERROR {e}", exc_info=True)
			return Response(
				ResponseDetail().errors_detail(error={"error": str(e)}),
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = menu_serializers.OptionSerializers(option, many=False).data
		return Response(
			ResponseDetail().success_detail(data=serializer, message="options has been updated successfully"),
			status=status.HTTP_200_OK)

	@action(
		methods=['DELETE'], url_path='option/(?P<option_id>[0-9]+)', detail=True,
		permission_classes=(permissions.IsAuthenticated, permissions.IsAdminUser)
	)
	def delete_option(self, request, pk=None, option_id=None):
		logger.info("delete a option to specific menu")
		instance = self.get_object()
		logger.info("delete specific option")
		try:
			menu_services.delete_option_menu(user=request.user, menu=instance.menu, option_id=option_id)
		except ValueError as e:
			logger.error(f"ValueError: {e}", exc_info=True)
			return Response(
				ResponseDetail().errors_detail(code=400, message="ValueError", error=str(e)),
				status=status.HTTP_400_BAD_REQUEST)
		except NotFound as e:
			logger.error(f"NotFound: {e}", exc_info=True)
			return Response(
				ResponseDetail().not_found_detail(message=str(e)), status=status.HTTP_404_NOT_FOUND)
		except Exception as e:
			logger.error(f"Exception: INTERNAL SERVER ERROR {e}", exc_info=True)
			return Response(
				ResponseDetail().errors_detail(error={"error": str(e)}),
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		return Response(
			ResponseDetail().success_detail(message="options has been delete successfully"), status=status.HTTP_200_OK)

	@action(
		methods=['GET'], url_path='send-reminder', detail=True,
		permission_classes=(permissions.IsAuthenticated, permissions.IsAdminUser)
	)
	def send_reminder(self, request, pk=None):
		logger.info("send reminder menu to all employed")
		instance = self.get_object()
		if not instance.notification:
			if instance.menu.option_menu.count() > 0:
				menu_tasks.send_slack_notification.delay(instance.get_reminder_template(), instance.id)
			else:
				return Response(ResponseDetail().errors_detail(
					code=400, message="is not possible send message, please add options first."),
					status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(ResponseDetail().errors_detail(
				code=400, message="The reminder was sent previously, it cannot be sent again."),
				status=status.HTTP_400_BAD_REQUEST)
		return Response(ResponseDetail().success_detail(
			message="The reminder has sent correctly"), status=status.HTTP_200_OK)
