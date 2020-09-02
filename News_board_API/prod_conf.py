import os

from .base_conf import BaseConf


class ProdConf(BaseConf):
    import os

    DB_NAME = os.environ.get("DB_NAME")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")

    SECRET_KEY = os.environ.get("SECRET_KEY")

    DEBUG = False

    ALLOWED_HOSTS = ["news-board-api-1.herokuapp.com"]

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": "5432",
        }
    }
    import dj_database_url

    db = dj_database_url.config()
    DATABASES["default"].update(db)

    REDIS_HOST = "ec2-79-125-17-63.eu-west-1.compute.amazonaws.com"
    REDIS_PORT = "24509"
    REDIS_USER = "h"
    REDIS_PASSWORD = "pc52a3304dae7800a67cfee553cf6b61edaeff962d725834fce2e7175c84827e7"
    BROKER_URL = (
        "redis://h:pc52a3304dae7800a67cfee553cf6b61edaeff962d725834fce2e7175c84"
        "827e7@ec2-79-125-17-63.eu-west-1.compute.amazonaws.com:24509"
    )
    BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}
    CELERY_RESULT_BACKEND = (
        "redis://h:pc52a3304dae7800a67cfee553cf6b61edaeff962d725834"
        "fce2e7175c84827e7@ec2-79-125-17-63.eu-west-1.compute.amazonaws.com:24509"
    )
