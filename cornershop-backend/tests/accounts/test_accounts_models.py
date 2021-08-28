import pytest
from app.modules.accounts.models import User


@pytest.mark.django_db
def test_user_model_success(client, user_data):
	user = User.objects.create(**user_data)
	get_user = User.objects.get(id=user.id)
	assert User.objects.count() == 1
	assert get_user.first_name == user_data['first_name']

