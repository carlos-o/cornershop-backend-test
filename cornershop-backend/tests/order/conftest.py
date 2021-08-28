import pytest
from rest_framework.test import APIClient
from app.modules.accounts.models import User
from django.contrib.auth.models import Group
from app.modules.menu.models import Option, Menu, MenuUser
from app.modules.order.models import Order
from tests.utils import user_json_data, menu_json_data, option_json_data, user_admin_data, customization_json_data


@pytest.fixture
def create_test_user():
	user = User.objects.create(**user_json_data())
	return user


@pytest.fixture
def create_employed_user():
	user = User.objects.create(**user_json_data())
	user_type = Group.objects.get_or_create(name=User.USER_EMPLOYEE)
	user.groups.add(user_type[0])
	return user


@pytest.fixture
def create_admin_user():
	user = User.objects.create(**user_admin_data())
	user_type = Group.objects.get_or_create(name=User.USER_ADMIN)
	user.groups.add(user_type[0])
	return user


@pytest.fixture
def create_test_menu():
	menu = Menu.objects.create(**menu_json_data())
	return menu


@pytest.fixture
def create_test_option(create_test_menu):
	option = Option.objects.create(
		menu=create_test_menu,
		**option_json_data()
	)
	return option


@pytest.fixture
def customization_data():
	return customization_json_data()


@pytest.fixture
def order_data(customization_data):
	option = Option.objects.get(id=1)
	return {"optionId": option.id, **customization_data}


@pytest.fixture
def create_test_menu_user_notification(create_test_option, create_admin_user):
	menu_user = MenuUser.objects.create(
		menu_id=create_test_option.menu.id,
		user=create_admin_user,
		notification=True
	)
	return menu_user


@pytest.fixture
def create_test_order(create_test_option, create_employed_user, customization_data):
	order = Order.objects.create(
		option=create_test_option,
		user=create_employed_user,
		menu_id=create_test_option.menu.id,
		**customization_data
	)
	return order


@pytest.fixture
def rest_client():
	return APIClient()

