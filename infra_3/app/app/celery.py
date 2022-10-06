import os
from celery import Celery
from django.conf import settings

CELERY_REGISTER_TASK = [
        "worker.tasks.task_1",
        "worker.tasks.task_2"
]

 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery(
        "app", 
        backend='redis', 
        broker=os.environ.get('CELERY_BROKER_URL'),
        include=CELERY_REGISTER_TASK
)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)