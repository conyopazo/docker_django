#!/bin/bash
python3 -m pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
open -n http://127.0.0.1:8000/
python3 manage.py runserver