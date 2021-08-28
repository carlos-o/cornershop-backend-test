import pytest
from datetime import datetime, timedelta
from app.modules.accounts.models import User


@pytest.mark.django_db
def test_list_menu_success(rest_client, create_admin_user, create_test_menu_user):
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.get('/menu/')
	assert response.status_code == 200
	data = dict(response.data)
	assert data.get('count') == 1
	results = [dict(result) for result in data.get('results')]
	assert len(results) == 1
	menu = results[0]
	assert menu.get('name') == "Menu de ejemplo"
	assert menu.get('start_date') == datetime.now().strftime("%Y-%m-%d")


@pytest.mark.django_db
def test_get_menu_success(rest_client, create_admin_user, create_test_menu_user):
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.get('/menu/1/')
	assert response.status_code == 200
	data = response.data.get('data')
	assert data.get('id') == 1
	assert data.get('name') == "Menu de ejemplo"
	assert data.get('start_date') == datetime.now().strftime("%Y-%m-%d")


@pytest.mark.django_db
def test_get_menu_not_found(rest_client, create_admin_user, create_test_menu_user):
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.get('/menu/22/')
	assert response.status_code == 404
	assert response.data.get('message') == "Not found."


@pytest.mark.django_db
def test_create_menu_success(rest_client, create_admin_user, menu_data):
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.post('/menu/', menu_data, format='json')
	assert response.status_code == 201
	data = response.data.get('data')
	assert data.get('id') == 1
	assert data.get('name') == "Menu de ejemplo"


@pytest.mark.django_db
def test_create_menu_failure(rest_client, create_admin_user):
	menu_data = {
		"description": "",
		"start_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
	}
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.post('/menu/', menu_data, format='json')
	assert response.status_code == 400
	data = response.data.get('errors')
	assert data.get('description')[0] == "empty values not allowed"
	assert data.get('name')[0] == "required field"
	assert data.get('start_date')[0] == "start date cannot is less than the current date"


@pytest.mark.django_db
def test_update_menu_success(rest_client, create_admin_user, create_test_menu_user):
	menu_data = {
		"name": "Menu del dia",
		"description": "sorprendeme",
		"start_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
	}
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.put('/menu/1/', menu_data, format='json')
	assert response.status_code == 200
	data = response.data.get('data')
	assert data.get('id') == 1
	assert data.get('name') == menu_data.get('name')


@pytest.mark.django_db
def test_update_menu_failure(rest_client, create_admin_user, create_test_menu_user, menu_data):
	menu_data = {
		"name": "",
		"description": "sorprendeme",
		"start_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
	}
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.put('/menu/1/', menu_data, format='json')
	assert response.status_code == 400
	data = response.data.get('errors')
	assert data.get('name')[0] == "empty values not allowed"
	assert data.get('start_date')[0] == "start date cannot is less than the current date"


@pytest.mark.django_db
def test_create_option_success(rest_client, create_admin_user, create_test_menu_user, option_data):
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.post('/menu/1/option/', option_data, format='json')
	assert response.status_code == 201
	data = response.data.get('data')
	assert data.get('id') == 1
	assert data.get('description') == "Ejemplo de una opcion de platillo"
	response = rest_client.get('/menu/1/')
	assert response.status_code == 200
	data = response.data.get('data')
	assert len(data.get('options')) == 1


@pytest.mark.django_db
def test_create_option_failure(rest_client, create_admin_user, create_test_menu_user):
	option_data = {}
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.post('/menu/1/option/', option_data, format='json')
	assert response.status_code == 400
	data = response.data.get('errors')
	assert data.get('description')[0] == "required field"
	response = rest_client.get('/menu/1/')
	assert response.status_code == 200
	data = response.data.get('data')
	assert len(data.get('options')) == 0


@pytest.mark.django_db
def test_update_option_success(rest_client, create_admin_user, create_test_menu_user, create_test_menu_option):
	option_data = {"description": "lasaña boloñesa"}
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.put('/menu/1/option/1/', option_data, format='json')
	assert response.status_code == 200
	data = response.data.get('data')
	assert data.get('id') == 1
	assert data.get('description') == option_data.get('description')


@pytest.mark.django_db
def test_update_option_failure(rest_client, create_admin_user, create_test_menu_user, create_test_menu_option):
	option_data = {"description": ""}
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.put('/menu/1/option/1/', option_data, format='json')
	assert response.status_code == 400
	data = response.data.get('errors')
	assert data.get('description')[0] == "empty values not allowed"


@pytest.mark.django_db
def test_update_option_not_found(rest_client, create_admin_user, create_test_menu_user, create_test_menu_option):
	option_data = {"description": "lasaña boloñesa"}
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.put('/menu/1/option/122/', option_data, format='json')
	assert response.status_code == 404
	assert response.data.get('message') == "Option does not exist in specific menu"


@pytest.mark.django_db
def test_update_option_deleted(rest_client, create_admin_user, create_test_menu_user, create_test_menu_option):
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.delete('/menu/1/option/1/')
	assert response.status_code == 200
	assert response.data.get('message') == "options has been delete successfully"

