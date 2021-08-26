from django.urls import path
from app.modules.order import views

urlpatterns = [
	path('', views.OrderListCreateView.as_view(), name='order'),
]
