celery_config.py
from kombu import Exchange, Queue

CELERY_TASK_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('reports', Exchange('reports'), routing_key='reports.process')
)

CELERY_TASK_ROUTES = {
    'process_blood_report': {'queue': 'reports', 'routing_key': 'reports.process'}
}

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_BROKER_URL = 'redis://localhost:6379/0'

CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_ACKS_LATE = True
CELERY_WORKER_CONCURRENCY = 4