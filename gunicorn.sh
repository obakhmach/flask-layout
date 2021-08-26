#!/bin/sh
gunicorn "flaskr:create_app('test')"