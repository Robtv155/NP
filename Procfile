web: cd nuevo_proyecto && python manage.py collectstatic --noinput && gunicorn nuevo_proyecto.wsgi:application --chdir nuevo_proyecto --bind 0.0.0.0:$PORT
