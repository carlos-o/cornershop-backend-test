import pytest
from rest_framework.test import APIClient
from app.modules.accounts.models import User
from tests.utils import user_json_data, user_login_data, login_test_data


@pytest.fixture
def user_data():
	return user_json_data()


@pytest.fixture
def login_data():
	return login_test_data()


@pytest.fixture
def create_test_user():
	user = User.objects.create(**user_login_data())
	return user


@pytest.fixture
def rest_client():
	return APIClient()
