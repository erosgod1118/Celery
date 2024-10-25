import os 
import time 

from celery import Celery 

celeryApp = Celery(__name__,)
celeryApp.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
celeryApp.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

@celeryApp.task(name="create_task")
def create_task(pTaskType):
    time.sleep(int(pTaskType) * 10)
    return True