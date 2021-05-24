echo "MIGRATING DATABASE"
python manage.py migrate --settings=backend.settings.dev

echo "RUN gunicorn"
gunicorn --bind 0.0.0.0:8891 --log-level INFO backend.wsgi
