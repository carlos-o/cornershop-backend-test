from app.modules.menu import models as menu_models
from app.modules.accounts.models import User
from django.db import transaction, DatabaseError
from .validations import (
	ValidatorMenu, validate_option
)
from app.modules.utils.permissions import is_active_user
from app.modules.utils.exceptions import NotFound
import json
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


@is_active_user
def create_menu(data: dict, user: User) -> menu_models.Menu:
	"""
		create a menu to specific date

		:param data: menu information
		:type data: dict
		:param user: user in session
		:type user: User Model
		:return: a new menu
		:raises: ValueError
	"""
	# validate menu data
	validator = ValidatorMenu(data)
	if validator.validation() is False:
		errors = validator.mistakes()
		for value in errors:
			errors[value] = validator.change_value(errors[value])
		logging.error("ERROR: in information of user %s" % str(errors), exc_info=True)
		raise ValueError(json.dumps(errors))
	with transaction.atomic():
		try:
			menu = menu_models.Menu.objects.create(
				name=data.get('name'),
				description=None if data.get('description') is None else data.get('description'),
				start_date=data.get('start_date')
			)
		except Exception as e:
			logging.error(f"ERROR: to stored menu {e}", exc_info=True)
			raise ValueError(json.dumps({"error": f"An error occurred while saving menu {e}"}))
		try:
			menu_models.MenuUser.objects.create(
				menu=menu,
				user=user,
			)
		except Exception as e:
			logging.error(f"ERROR: to stored menu of user {e}", exc_info=True)
			raise ValueError(json.dumps({"error": f"An error occurred while saving menu of user {e}"}))
	logger.debug("menu has been created")
	return menu


@is_active_user
def update_menu(data: dict, menu_user: menu_models.MenuUser, user: User) -> menu_models.Menu:
	"""
		update menu information

		:param data: menu information
		:type data: dict
		:param menu_user: MenuUser object
		:type menu_user: MenuUser Model
		:param user: user in session
		:type user: User Model
		:return: Menu
		:raises: ValueError
	"""
	if menu_user.notification:
		raise ValueError(json.dumps({"error": "the menu cannot be updated because it has already been sent"}))
	validator = ValidatorMenu(data)
	if validator.validation() is False:
		errors = validator.mistakes()
		for value in errors:
			errors[value] = validator.change_value(errors[value])
		logging.error("ERROR: in information of user %s" % str(errors), exc_info=True)
		raise ValueError(json.dumps(errors))
	menu_user.menu.name = data.get('name')
	menu_user.menu.description = data.get('description')
	menu_user.menu.start_date = data.get('start_date')
	menu_user.menu.save()
	return menu_user.menu


@is_active_user
def create_option_menu(data: dict, user: User, menu: menu_models.Menu) -> menu_models.Option:
	"""
		create a new option for specific menu

		:param data: option description
		:type data: dict
		:param user: user is session
		:type user: User Model
		:param menu: Menu Object
		:type menu: Menu Model
		:return: new option
		:raises: ValueError
	"""
	# validate option
	validate_option(data)
	# create a new option
	try:
		option = menu_models.Option.objects.create(
			menu_id=menu.id,
			description=data.get('description')
		)
	except Exception as e:
		logging.error(f"ERROR: to stored menu of user {e}", exc_info=True)
		raise ValueError(json.dumps({"error": f"An error occurred while saving option of menu {e}"}))
	logger.debug("option has been added")
	return option


@is_active_user
def update_option_menu(data: dict, user: User, menu: menu_models.Menu, option_id: int) -> menu_models.Option:
	"""
		Update specific option of specific menu

		:param data: option description
		:type data: dict
		:param user: user is session
		:type user: User Model
		:param menu: Menu Object
		:type menu: Menu Model
		:param option_id: id of option
		:type option_id: int
		:return: edited option
		:raises: ValueError, NotFound
	"""
	# validate option
	validate_option(data)
	# check if option exist
	option = menu_models.Option.objects.filter(id=option_id, menu_id=menu.id).first()
	if option is None:
		raise NotFound("Option does not exist in specific menu")
	# update a new option
	option.description = data.get('description')
	option.save()
	logger.debug("option has been updated")
	return option


@is_active_user
def delete_option_menu(user: User, menu: menu_models.Menu, option_id: int) -> menu_models.Option:
	"""
		delete specific option of specific menu

		:param user: user is session
		:type user: User Model
		:param menu: Menu Object
		:type menu: Menu Model
		:param option_id: id of option
		:type option_id: int
		:return: edited option
		:raises: ValueError, NotFound
	"""
	# check if option exist
	option = menu_models.Option.objects.filter(id=option_id, menu_id=menu.id).first()
	if option is None:
		raise NotFound("Option does not exist in specific menu")
	# update a new option
	option.delete()
	logger.debug("option has been delete")
	return option
