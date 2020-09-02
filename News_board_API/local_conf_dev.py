import os

from .base_conf import BaseConf


class LocalConf(BaseConf):
    DEBUG = True
    SECRET_KEY = "pys^v=+5+!bj4w9%5uxoq2mp@mp9&hybspq_i3fd&jev!z6h_u"

    REDIS_HOST = "redis"
    REDIS_PORT = "6379"
    BROKER_URL = "redis://" + REDIS_HOST + ":" + REDIS_PORT + "/0"
    BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}
    CELERY_RESULT_BACKEND = "redis://" + REDIS_HOST + ":" + REDIS_PORT + "/0"
