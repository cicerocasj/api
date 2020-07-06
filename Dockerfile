FROM python:3.8.3
RUN mkdir /code
ADD requirements.txt /code
RUN pip install -r /code/requirements.txt
ADD . /code
WORKDIR /code
VOLUME /code

ENTRYPOINT bash -c "python manage.py migrate --noinput && python manage.py makemigrations --noinput && python manage.py runserver 0.0.0.0:8000"
