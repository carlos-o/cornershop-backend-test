from django.contrib import admin
from app.modules.accounts.models import User
from django.contrib.auth.admin import UserAdmin as UserAdminProfile


class UserAdmin(UserAdminProfile):
	"""
	register the information of the fields of the user account in django admin.
	"""

	class Meta:
		model = User
		ordering = ('id',)

	fieldsets = (
		(None, {'fields':
					('username', 'first_name', 'last_name', 'email', 'address', 'phone', 'rut')
				}),
		(('Permissions'), {'fields':
							   ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
						   }),
	)
	list_display = ('id', 'username', 'email', 'rut', 'created_at', 'is_active')
	search_fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'rut')
	list_filter = ('created_at',)

	def get_ordering(self, request):
		return ['id']


admin.site.register(User, UserAdmin)
