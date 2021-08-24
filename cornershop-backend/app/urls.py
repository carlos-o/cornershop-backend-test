"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.modules.accounts import urls as account_urls
from app.modules.menu import urls as menu_urls
from app.modules.menu import views as menu_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'option', menu_views.OptionReadOnlyViewSet)
router.register(r'menu', menu_views.MenuViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(account_urls)),
    path('', include(router.urls)),
]
