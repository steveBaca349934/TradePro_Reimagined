#!/bin/bash
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"smbaca99@gmail.com"}
cd /app/

/opt/tradepro_venv/bin/python3 manage.py migrate --noinput
/opt/tradepro_venv/bin/python3 manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

