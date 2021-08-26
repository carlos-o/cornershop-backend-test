from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import MenuUser
from app.settings import (
	SLACK_TOKEN,
	SLACK_CHANNEL
)
from slack import WebClient
from slack.errors import SlackApiError
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_slack_notification(message: str, menu_user_id: int) -> bool:
	"""
		send messages to slack with the menu and their options for all employees

		:param message: message to send
		:type message: str
		:param menu_user_id: id of menu_user
		:type menu_user_id: int
		:return: True
	"""
	client = WebClient(token=SLACK_TOKEN)
	try:
		client.chat_postMessage(
			channel=SLACK_CHANNEL,
			text=message
		)
	except SlackApiError as e:
		logger.error(f"Got an error: {e.response['error']}")
		print(f"Got an error: {e.response['error']}")
		return False
	menu_user = MenuUser.objects.get(id=menu_user_id)
	menu_user.notification = True
	menu_user.save()
	return True
