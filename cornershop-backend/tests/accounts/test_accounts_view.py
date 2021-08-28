import pytest
from app.modules.accounts.models import User


@pytest.mark.django_db
def test_login_success(client, create_test_user, login_data):
	assert User.objects.count() == 1
	response = client.post('/accounts/signin/', login_data, headers={"Content-Type": "application/json"})
	data = response.data.get('data')
	assert response.status_code == 200
	assert data.get('id') == 1
	assert data.get('username') == login_data["username"]


@pytest.mark.django_db
def test_login_failure(client, create_test_user):
	assert User.objects.count() == 1
	data = {"username": "example", "password": "example"}
	response = client.post('/accounts/signin/', data, headers={"Content-Type": "application/json"})
	assert response.status_code == 400
	assert response.data.get('errors') == 'The username or password is incorrect'


@pytest.mark.django_db
def test_login_failure(client, create_test_user):
	assert User.objects.count() == 1
	data = {"username": "example", "password": "example"}
	response = client.post('/accounts/signin/', data, headers={"Content-Type": "application/json"})
	assert response.status_code == 400
	assert response.data.get('errors') == 'The username or password is incorrect'


@pytest.mark.django_db
def test_login_failure_username(client, create_test_user):
	assert User.objects.count() == 1
	data = {"username": "", "password": "example"}
	response = client.post('/accounts/signin/', data, headers={"Content-Type": "application/json"})
	assert response.status_code == 400
	assert response.data.get('errors').get('username') == 'The username field cannot be empty'


@pytest.mark.django_db
def test_login_failure_password(client, create_test_user):
	assert User.objects.count() == 1
	data = {"username": "example", "password": ""}
	response = client.post('/accounts/signin/', data, headers={"Content-Type": "application/json"})
	assert response.status_code == 400
	assert response.data.get('errors').get('password') == 'The password field cannot be empty'


@pytest.mark.django_db
def test_logout_success(rest_client, create_test_user, login_data):
	assert User.objects.count() == 1
	response = rest_client.post('/accounts/signin/', login_data, format='json')
	data = response.data.get('data')
	assert response.status_code == 200
	assert data.get('id') == 1
	assert data.get('username') == login_data["username"]
	rest_client.force_authenticate(user=create_test_user, token=data.get('token'))
	response = rest_client.post('/accounts/signout/')
	assert response.status_code == 200
	assert response.data.get("message") == "ok"


@pytest.mark.django_db
def test_logout_failure(rest_client, create_test_user, login_data):
	assert User.objects.count() == 1
	response = rest_client.post('/accounts/signin/', login_data, format='json')
	data = response.data.get('data')
	assert response.status_code == 200
	assert data.get('id') == 1
	assert data.get('username') == login_data["username"]
	response = rest_client.post('/accounts/signout/')
	assert response.status_code == 401
