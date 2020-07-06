FROM python:3.8.3
RUN mkdir /app
WORKDIR /app
ADD . /app/
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV PORT=8000
EXPOSE 8000
CMD gunicorn cfehome.wsgi:application --bind 0.0.0.0:$PORT
