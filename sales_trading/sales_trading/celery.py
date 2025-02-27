from celery.schedules import crontab
from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sales_trading.settings")

app = Celery("sales_trading")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "delete-inactive-users-every-day": {
        "task": "users.tasks.delete_inactive_users",
        "schedule": crontab(hour=0, minute=0),  # Каждый день в полночь
    },
}
