FROM python:3.8-alpine
MAINTAINER Oleksandr Bakhmach "alexandrbakhmach@gmail.com"

WORKDIR /app

RUN mkdir flaskr

COPY ./flaskr ./flaskr
COPY ./setup.py .
COPY ./MANIFEST.in .
COPY ./instance/config.py /app/instance/config.py

ENV INSTANCE_PATH=/app/instance

RUN pip install gunicorn

RUN python setup.py bdist_wheel
RUN pip install dist/flaskr*
RUN rm -rf flaskr
RUN rm setup.py
RUN rm MANIFEST.in
RUN rm -rf dist
RUN rm -rf build
RUN rm -rf flaskr.egg-info

COPY ./gunicorn.conf.py .
COPY ./gunicorn.sh .

CMD ["./gunicorn.sh"]