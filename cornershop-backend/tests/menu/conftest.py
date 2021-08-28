import pytest
from rest_framework.test import APIClient
from app.modules.accounts.models import User
from app.modules.menu.models import Menu, MenuUser, Option
from tests.utils import user_json_data, menu_json_data, option_json_data, user_admin_data, login_test_data


@pytest.fixture
def option_data():
	return option_json_data()


@pytest.fixture
def create_test_user():
	user = User.objects.create(**user_json_data())
	return user


@pytest.fixture
def menu_data():
	return menu_json_data()


@pytest.fixture
def create_admin_user():
	user = User.objects.create(**user_admin_data())
	return user


@pytest.fixture
def create_test_menu(menu_data):
	menu = Menu.objects.create(**menu_data)
	return menu


@pytest.fixture
def create_test_menu_user(create_test_menu, create_admin_user):
	menu_user = MenuUser.objects.create(
		menu=create_test_menu,
		user=create_admin_user
	)
	return menu_user


@pytest.fixture
def create_test_menu_option(create_test_menu, option_data):
	option = Option.objects.create(menu=create_test_menu, **option_data)
	return option


@pytest.fixture
def login_data():
	return login_test_data()


@pytest.fixture
def rest_client():
	return APIClient()

