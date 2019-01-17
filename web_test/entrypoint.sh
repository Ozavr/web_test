#!/bin/sh

python manage.py runserver & python manage.py rqworker tasks_queue_1 & python manage.py rqworker tasks_queue_2