# Flask 2.0 project layout
## How to setup
- In flask-layout/instance folder create the config.py setting file.
    ```
    $ cp example.config.py config.py
    ```
- Ensure you have python installed and ready with gunicorn and **flask >= 2.0**.
- To run the application locally with the flask you need firstly install the application as the python library. Also, it is suggested to use the virtual environment. Use all commands in the root project directory.
    ```
    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -e .
    $ export FLASK_APP=flaskr
    $ export FLASK_ENV=development
    ```
    and finally, run the application.
    ```
    $ flask run
    ```
- The deployment process can be illustrated by creating the docker container and running it.
  To create the docker container run the following command in the root directory.
    ```
    $ docker build -t flask-layout .
    ```
  To run the docker container just execute
  ```
  $ docker run -p 8000:8000 -d --name=flask-layout-instance flask-layout
  ```
- When the application will be running either locally or in docker it can be accessed on port 8000.