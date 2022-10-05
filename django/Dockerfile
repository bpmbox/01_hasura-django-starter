FROM python:3
ENV PIP_NO_CACHE_DIR=1
RUN pip install --upgrade pip && pip install 'django<4' \
        'djangorestframework<4' \
        'djangorestframework-simplejwt<5' \
        'django-rest-swagger' \
        'django-import-export<3' \
        'django-rest-passwordreset<2' \
        'psycopg2<3' \
        'gunicorn<21' \
        'django-cors-headers<4' \
        'requests<3' \
        'uuid<2' \
        'drf-yasg' \
        'django-filter' \
        'fastapi' \
        'pydantic' \
        'uvicorn' \
        'uvloop' \
        'whitenoise' \
        'django-stubs' \
        'mangum'

WORKDIR /code
ADD ./entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
CMD ["uvicorn", "app.asgi:fastapp", "--host", "0.0.0.0", "--port", "8000"]