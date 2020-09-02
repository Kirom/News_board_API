# News_board_API
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python test assessment for DevelopsToday.

Deployment link: `https://news-board-api-1.herokuapp.com/` or [click](https://news-board-api-1.herokuapp.com/).

Postman collection link: `https://www.getpostman.com/collections/884be669324a50c8151d`

Postman environments files in json format are `News board deploy.postman_environment.json` and `News board develop.postman_environment.json`

If you cannot run via Docker by first instruction, use second instruction then.
## 1) Running Docker's containers steps
1. Clone repo: `git clone https://github.com/Kirom/News_board_API.git`
2. Rename `local_conf_dev.py` to `local_conf.py`
3. Create virtualenv, for example: `python3 -m venv venv` or `virtualenv -p python3 venv`
4. Activate it `source venv/bin/activate`
5. Run Docker compose: `docker-compose up`
## 2) Running without docker step by step
1. Clone repo: `git clone https://github.com/Kirom/News_board_API.git`
2. Rename `local_conf_dev.py` to `local_conf.py`
3. Change `REDIS_HOST = "redis"` variable in local_conf.py file to `REDIS_HOST = "localhost"`
4. Create virtualenv, for example: `python3 -m venv venv` or `virtualenv -p python3 venv`
4. Activate it `source venv/bin/activate`
5. Install all the packages `pip install -r requirements.txt`
6. Run redis `redis-server`
7. Run celery worker `celery -A News_board_API worker -l info -B`
8. Start the app itself `./manage.py runserver`

