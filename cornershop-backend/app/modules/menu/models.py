from django.db import models
from uuid import uuid4
from app.modules.accounts.models import User
from app.settings import WEBSITE_URL
from django.utils.translation import gettext as _


class Menu(models.Model):
	uuid = models.UUIDField(default=uuid4, editable=False)
	name = models.CharField(_("Name"), max_length=100, blank=False, null=False)
	start_date = models.DateField(default=None)
	description = models.CharField(_("Description"), max_length=255, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		ordering = ['created_at']

	def __str__(self):
		return f"{self.name}-{self.id}"


class MenuUser(models.Model):
	user = models.ForeignKey(User, related_name='user_menu', on_delete=models.CASCADE, blank=False, null=False)
	menu = models.ForeignKey(Menu, related_name='menu_user', on_delete=models.CASCADE, blank=False, null=False)
	notification = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		unique_together = ('user', 'created_at')
		ordering = ['created_at']

	def get_reminder_template(self):
		template = ""
		if self.menu.option_menu.count():
			url = WEBSITE_URL + f'/menu/{self.menu.uuid}'
			template += url
			template += """\n\nHello! \nI share with you today's menu :) \n\n"""
			for key, value in enumerate(self.menu.option_menu.all()):
				template += f"Option {key+1}: {value}.\n"
			template += "\nHave a nice day!"
		return template


class Option(models.Model):
	menu = models.ForeignKey(Menu, related_name='option_menu', on_delete=models.CASCADE, blank=False, null=False)
	description = models.CharField(max_length=255, blank=False, null=False)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		ordering = ['created_at']

	def __str__(self):
		return self.description
