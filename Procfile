web: gunicorn News_board_API.wsgi --log-file -
celery: celery worker -A News_board_API -l info -c 4 -B