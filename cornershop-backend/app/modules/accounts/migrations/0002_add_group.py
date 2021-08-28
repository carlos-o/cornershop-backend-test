from django.db import models, migrations


def group_migration(apps, schema_editor):
    group = apps.get_model('auth', 'Group')
    group.objects.bulk_create([
        group(name=u'Admin'),
        group(name=u'Employee'),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(group_migration)
    ]
