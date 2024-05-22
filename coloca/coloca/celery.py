import os
from celery import Celery
from datetime import timedelta
from .utils import updateDB

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coloca.settings")

app = Celery('coloca')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_default_rate_limit = '10/m'
# app.conf.task_routes = {'coloca.celery.func': {'queue': 'queue1'}}
# app.conf.task_routes = {'newapp.tasks.task': {'queue': 'queue1'}}


# Task schedule config
app.conf.beat_schedule = {
    'sch_task1': {
        'task': 'coloca.celery.task1',
        'schedule': timedelta(minutes=5),  # 5-minutes interval
    },
}

# Scheduled task


@app.task
def task1():
    print('Initializing periodic task (Update Joke)')
    result = updateDB()
    print('(Update Joke) Task finished -> ', result)


app.autodiscover_tasks()
