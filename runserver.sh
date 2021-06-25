#!/bin/bash

echo "RUN SERVER"
# wait mysql

bash ./wait-for-it.sh -h db_postgres -p 5432 -t 60

sleep 5

python manage.py makemigrations

python manage.py migrate

python manage.py makemigrations --merge

export DJANGO_SUPERUSER_PASSWORD=admin

python manage.py createsuperuser --no-input --username admin --email email@mysite.com

python manage.py runserver 0.0.0.0:8000