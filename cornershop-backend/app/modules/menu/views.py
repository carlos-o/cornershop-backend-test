from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.generics import (
	RetrieveUpdateDestroyAPIView,
	ListAPIView,
	ListCreateAPIView
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework import (
	permissions,
	status
)
from rest_framework.response import Response
from app.modules.utils.response import ResponseDetail
from app.modules.utils.exceptions import NotFound
from app.modules.utils.pagination import CustomPagination
from django.core.exceptions import PermissionDenied
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
		queryset = menu_models.MenuUser.objects.filter(user_id=self.request.user.id).order_by('-created_at')
		return queryset

	def list(self, request, *args, **kwargs):
		paginator = CustomPagination()
		context = paginator.paginate_queryset(self.queryset, request)
		serializer = self.get_serializer(context, many=True).data
		return paginator.get_paginated_response(serializer)

	def retrieve(self, request, *args, **kwargs):
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

	@action(
		methods=['POST'], url_path='option', detail=True,
		permission_classes=(permissions.IsAuthenticated, permissions.IsAdminUser)
	)
	def add_option(self, request, pk=None):
		instance = self.get_object()
		logger.info("add option to specific menu")
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

	# def update(self, request, *args, **kwargs):
	# 	instance = self.get_object()
	# 	try:
	# 		user = accounts_services.update(request.data, instance, request.user)
	# 	except ValueError as e:
	# 		return Response(ResponseDetail().errors_detail(code=400, message="ValueError", error=str(e)),
	# 						status=status.HTTP_400_BAD_REQUEST)
	# 	except Exception as e:
	# 		logger.error("Exception: INTERNAL SERVER ERROR %s" % str(e), exc_info=True)
	# 		return Response(ResponseDetail().errors_detail(error={"error": str(e)}),
	# 						status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	# 	serializer = self.get_serializer(user, many=False).data
	# 	return Response(ResponseDetail().success_detail(data=serializer, message="You have edit user data correctly"),
	# 					status=status.HTTP_200_OK)
	#
	# def destroy(self, request, *args, **kwargs):
	# 	instance = self.get_object()
	# 	try:
	# 		accounts_services.destroy(instance, user_session=request.user)
	# 	except ValueError as e:
	# 		return Response(ResponseDetail().errors_detail(code=400, message="ValueError", error=str(e)),
	# 						status=status.HTTP_400_BAD_REQUEST)
	# 	except Exception as e:
	# 		logger.error("Exception: INTERNAL SERVER ERROR %s" % str(e), exc_info=True)
	# 		return Response(ResponseDetail().errors_detail(error={"error": str(e)}),
	# 						status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	# 	accounts_tasks.send_notification.apply_async(
	# 		args=[instance.email, "email/deleted_account.html", 'Account deleted'], countdown=30)
	# 	return Response(ResponseDetail().success_detail(message="The user has been delete correctly"),
	# 					status=status.HTTP_200_OK)


class OptionReadOnlyViewSet(ReadOnlyModelViewSet):
	permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
	serializer_class = menu_serializers.OptionSerializers
	queryset = menu_models.Option.objects.all()

	def list(self, request, *args, **kwargs):
		paginator = CustomPagination()
		context = paginator.paginate_queryset(self.queryset, request)
		serializer = self.get_serializer(context, many=True).data
		return paginator.get_paginated_response(serializer)

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response(ResponseDetail().success_detail(data=serializer.data), status=status.HTTP_200_OK)
