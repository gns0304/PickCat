#!/bin/bash

python manage.py migrate

uwsgi --http 0.0.0.0:8000 --module PickCat.wsgi --workers 32 --threads 4
