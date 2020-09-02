"""Celery's config file."""
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "News_board_API.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "LocalConf")
import configurations  # noqa

configurations.setup()

app = Celery("News_board_API")
app.config_from_object("django.conf:settings")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "run-every-day": {
        "task": "api.tasks.clean_upvotes",
        "schedule": crontab(minute=0, hour=0),
    },
}
