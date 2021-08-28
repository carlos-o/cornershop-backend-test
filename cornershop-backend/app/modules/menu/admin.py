from django.contrib import admin
from app.modules.menu.models import Menu, MenuUser, Option
# Register your models here.

admin.site.register(Menu)

admin.site.register(MenuUser)

admin.site.register(Option)
