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
