"""Gunicorn configuration file
All configuration of threads and processes must
be placed here.
"""

import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
chdir = "."
threads = 1