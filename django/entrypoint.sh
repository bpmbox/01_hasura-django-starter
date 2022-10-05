#!/bin/bash -x
# echo "Static Files"
# python manage.py collectstatic --noinput
echo "Make Migrations"
python manage.py makemigrations --noinput
echo "Migrate DB"
python manage.py migrate --noinput || exit 1
echo "Start server"
uvicorn app.asgi:fastapp --reload