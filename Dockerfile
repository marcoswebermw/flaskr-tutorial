FROM python:latest

ADD . /code

WORKDIR /code

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=flaskr
ENV FLASK_ENV=development
#ENV FLASK_DEBUG=1

EXPOSE 5000

