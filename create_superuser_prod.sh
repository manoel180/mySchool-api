#!/bin/bash

python manage.py migrate --run-syncdb
python manage.py collectstatic --no-input

python manage.py createsuperuser --username=${DJANGO_SUPERUSER_NAME} --email=${DJANGO_SUPERUSER_EMAIL} --noinput

gunicorn mySchool.wsgi:application --bind 0.0.0.0:8080 --preload
