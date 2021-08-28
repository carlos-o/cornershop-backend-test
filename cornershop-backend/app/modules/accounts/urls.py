from django.urls import path
from app.modules.accounts import views

urlpatterns = [
	path('signin/', views.login_view, name='login'),
	path('signout/', views.logout_view, name='logout'),
]
