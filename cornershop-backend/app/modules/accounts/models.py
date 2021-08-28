from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
	"""
		the model class to store all user information.
	"""
	USER_ADMIN = "Admin"
	USER_EMPLOYEE = "Employee"
	USER_TYPES = (
		(USER_ADMIN, _("Admin")),
		(USER_EMPLOYEE, _("Employee"))
	)
	phone = models.CharField(_('Phone'), max_length=16, blank=True, null=True)
	address = models.CharField(_('Address'), max_length=255, blank=True, null=True)
	rut = models.CharField(_('Rut'), max_length=15, blank=False, null=False, unique=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	deleted_at = models.DateTimeField(blank=True, null=True)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.username
