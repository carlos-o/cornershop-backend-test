from django.db import models
from app.modules.accounts.models import User
from app.modules.menu.models import Option
from django.utils.translation import gettext as _


class Order(models.Model):
	user = models.ForeignKey(User, related_name='user_order', on_delete=models.CASCADE, blank=True, null=True)
	option = models.ForeignKey(Option, related_name='option_order', on_delete=models.CASCADE, blank=True, null=True)
	menu_id = models.IntegerField(_("Menu"), blank=False, null=False, default=0)
	customization = models.CharField(_("Customization"), max_length=255, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		ordering = ['created_at']

	def __str__(self):
		return str(self.id)
