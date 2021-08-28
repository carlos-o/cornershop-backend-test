import string
from datetime import datetime
from app.modules.utils.services import code_generator
from django.contrib.auth.hashers import make_password


username = "soulrac"
password = make_password("Car1234*")
first_name = "carlos"
last_name = "olivero"
email = code_generator(size=15) + "@gmail.com"
rut = "26661495-0"


def login_test_data():
	return {
		"username": username,
		"password": "Car1234*",
	}


def user_login_data():
	return {
		"username": username,
		"password": password,
		"first_name": first_name,
		"last_name": last_name,
		"email": email,
		"rut": rut
	}


def user_admin_data():
	return {
		**user_login_data(),
		"is_staff": True,
		"is_superuser": True
	}


def user_json_data():
	return {
		"username": code_generator(size=10),
		"password": make_password(code_generator(size=8)),
		"first_name": first_name,
		"last_name": last_name,
		"email": code_generator(size=15) + "@gmail.com",
		"rut": code_generator(size=10, chars=string.digits)
	}


def menu_json_data():
	return {
		"name": "Menu de ejemplo",
		"description": "Ejemplo",
		"start_date": datetime.now().strftime("%Y-%m-%d")
	}


def option_json_data():
	return {
		"description": "Ejemplo de una opcion de platillo"
	}


def customization_json_data():
	return {
		"customization": "agregar mucha cantidad"
	}
