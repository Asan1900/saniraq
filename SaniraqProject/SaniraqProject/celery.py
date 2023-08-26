import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SaniraqProject.settings.development')

celery_app = Celery('SaniraqProject')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks(related_name='tasks')