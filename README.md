# Celery
Celery Python FastAPI

# Version
Python v3.8
Ubuntu 20 LTS

# Commands
uvicorn main:app --host 0.0.0.0 --reload
celery -A tasks worker --loglevel=info