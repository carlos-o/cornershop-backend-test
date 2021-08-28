import pytest
from app.modules.accounts.models import User
from app.modules.order.models import Order
from app.modules.menu.models import Option, Menu


@pytest.mark.django_db
def test_option_model_success(client, create_test_user, create_test_option):
	user = User.objects.get(id=1)
	option = Option.objects.get(id=1)
	customization = "con mucho queso"
	order = Order.objects.create(
		user=user,
		option=option,
		menu_id=option.menu.id,
		customization=customization
	)
	assert Order.objects.count() == 1
	assert order.customization == customization
