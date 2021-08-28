import os
from celery import Celery
from .settings import DEBUG

settings = 'app.development' if DEBUG else 'app.production'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
