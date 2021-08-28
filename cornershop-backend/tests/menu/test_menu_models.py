import pytest
from app.modules.accounts.models import User
from app.modules.menu.models import Menu, Option, MenuUser


@pytest.mark.django_db
def test_menu_model_success(client, menu_data):
	menu = Menu.objects.create(**menu_data)
	assert Menu.objects.count() == 1
	assert menu.name == "Menu de ejemplo"


@pytest.mark.django_db
def test_option_model_success(client, menu_data, option_data):
	menu = Menu.objects.create(**menu_data)
	option = Option.objects.create(
		menu=menu,
		**option_data
	)
	assert Option.objects.count() == 1
	assert option.description == "Ejemplo de una opcion de platillo"


@pytest.mark.django_db
def test_menu_user_model_success(client, create_test_menu, create_test_user):
	user = User.objects.get(id=1)
	menu_user = MenuUser.objects.create(
		menu=create_test_menu,
		user=user
	)
	assert MenuUser.objects.count() == 1
	assert menu_user.menu.name == "Menu de ejemplo"
	assert menu_user.user.first_name == "carlos"

