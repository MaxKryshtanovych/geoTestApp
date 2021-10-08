import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geoTest.settings')

app = Celery('geoTest')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'run-every-single-minute': {
        'task': 'core.tasks.check_amount',
        'schedule': crontab(),
    },
}

app.autodiscover_tasks()
