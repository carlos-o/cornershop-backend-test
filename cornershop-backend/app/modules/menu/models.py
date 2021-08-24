from django.db import models
from uuid import uuid4
from app.modules.accounts.models import User
from django.utils.translation import ugettext_lazy as _


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

	def __str__(self):
		return self.menu.name


class Option(models.Model):
	menu = models.ForeignKey(Menu, related_name='option_menu', on_delete=models.CASCADE, blank=False, null=False)
	description = models.CharField(max_length=255, blank=False, null=False)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		ordering = ['created_at']

	def __str__(self):
		return self.description
