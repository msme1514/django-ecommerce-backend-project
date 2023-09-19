release: python manage.py migrate
web: gunicorn storefront.wsgi
worker: celery -A storefront worker -l info -P gevent
web: python manage.py collectstatic --noinput; gunicorn storefront.wsgi
