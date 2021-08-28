import pytest


@pytest.mark.django_db
def test_list_order_success(rest_client, create_admin_user, create_test_order):
	rest_client.force_authenticate(create_admin_user)
	response = rest_client.get('/order/')
	assert response.status_code == 200
	data = dict(response.data)
	assert data.get('count') == 1
	results = [dict(result) for result in data.get('results')]
	assert len(results) == 1
	order = results[0]
	assert order.get('menu') == "Menu de ejemplo"
	assert order.get('name') == "carlos olivero"
	assert order.get('option') == "Ejemplo de una opcion de platillo"
	assert order.get('customization') == "agregar mucha cantidad"


@pytest.mark.django_db
def test_create_order_success(rest_client, create_employed_user, create_test_menu_user_notification, order_data):
	rest_client.force_authenticate(create_employed_user)
	response = rest_client.post('/order/', order_data, format='json')
	assert response.status_code == 201
	data = response.data.get('data')
	assert data.get('id') == 1
	assert data.get('menu') == "Menu de ejemplo"
	assert data.get('option') == "Ejemplo de una opcion de platillo"
	assert data.get('customization') == "agregar mucha cantidad"


@pytest.mark.django_db
def test_create_order_failure(rest_client, create_employed_user, create_test_order):
	rest_client.force_authenticate(create_employed_user)
	# test order all ready create
	order_data = {"optionId": 1, "customization": "agregar mucha cantidad"}
	response = rest_client.post('/order/', order_data, format='json')
	assert response.status_code == 400
	error = response.data.get('errors')
	assert error.get('error') == 'order from specific menu all ready create'
	# test option not exist
	order_data = {"optionId": 99, "customization": "agregar mucha cantidad"}
	response = rest_client.post('/order/', order_data, format='json')
	assert response.status_code == 400
	error = response.data.get('errors')
	assert error.get('optionId') == 'option of the menu does not exist'
	# test validate fields
	order_data = {"optionId": "99", "customization": ""}
	response = rest_client.post('/order/', order_data, format='json')
	assert response.status_code == 400
	error = response.data.get('errors')
	assert error.get('optionId')[0] == 'must be of integer type'
	assert error.get('customization')[0] == 'empty values not allowed'
