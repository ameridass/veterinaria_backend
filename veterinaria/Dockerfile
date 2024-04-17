FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

copy requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY veterinaria .

#RUN python manage.py migrate
#RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD python manage.py migrate && gunicorn -b 0.0.0.0:8000 veterinaria.wsgi:application