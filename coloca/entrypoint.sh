#!/bin/ash

echo "DB migrations"
python manage.py migrate

exec "$@"