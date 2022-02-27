#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/
/opt/tradepro_venv/bin/gunicorn --worker-tmp-dir /dev/shm TradePro_Reimagined.wsgi:application --bind "0.0.0.0:${APP_PORT}"