from app.modules.menu.models import Option
from app.modules.accounts.models import User
from .models import Order
from .validations import validate_order
from app.modules.utils.permissions import is_active_user
from datetime import datetime, time
import json
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


@is_active_user
def create_order(data: dict, user: User) -> Order:
	"""
		create a new order for the menu

		:param data: order information
		:type data: dict
		:param user: user employed in session
		:type user: User Model
		:return: Order object
		:raises: ValueError
	"""
	# Check the time limit to create the order, the limit time of day is 11am
	today_now = datetime.now()
	today_time = time(today_now.hour, today_now.minute, today_now.second)
	if today_time.hour > 10 and today_time.minute <= 60:
		raise ValueError(json.dumps({"error": "can't create order after 11 a.m"}))
	validate_order(data)
	# check if option all ready exists
	try:
		option = Option.objects.get(id=data.get('optionId'))
	except Exception as e:
		raise ValueError(json.dumps({"optionId": "option of the menu does not exist"}))
	menu_id = option.menu.id
	# check if order all ready create
	if Order.objects.filter(menu_id=menu_id).exists():
		raise ValueError(json.dumps({"error": "order from specific menu all ready create"}))
	# create order
	try:
		order = Order.objects.create(
			user=user,
			option_id=data.get('optionId'),
			menu_id=menu_id,
			customization=None if data.get('customization') is None else data.get('customization')
		)
	except Exception as e:
		logging.error(f"ERROR: to stored order {e}", exc_info=True)
		raise ValueError(json.dumps({"error": f"An error occurred while saving order {e}"}))
	return order

