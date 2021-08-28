from django.db import models, migrations
from django.contrib.auth.hashers import make_password


def user_migration(apps, schema_editor):
    user = apps.get_model('accounts', 'User')
    group = apps.get_model('auth', 'Group')
    # create admin user
    user_admin = user.objects.create(
        username="nora", first_name="nora", last_name="cornershop", rut="123456789-0",
        password=make_password("1234qwer*"), email="nora@cornershop.cl", is_staff=True, is_superuser=True
    )
    user_type_admin = group.objects.get(name="Admin")
    user_admin.groups.add(user_type_admin)

    # create employed user
    user_employed = user.objects.create(
        username="test", first_name="test", last_name="example",
        email="test@cornershop.cl", rut="987654321-0", password=make_password("Test1234*")
    )
    user_type_employed = group.objects.get(name="Employee")
    user_employed.groups.add(user_type_employed)


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_add_group'),
    ]

    operations = [
        migrations.RunPython(user_migration)
    ]
