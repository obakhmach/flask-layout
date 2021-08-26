import os

from flask import Flask
from typing import Dict


def create_app(env: str = None, test_config=None) -> Flask:
    """Function that is the realization of the
    factory method pattern

    Args:
        env (str): The string which specify current environment.

    Returns:
        Flask: The instance of the flask app.
    """
    instance_path = os.environ.get('INSTANCE_PATH', None)

    if instance_path is None:
        raise ValueError('Instance path must be set.')

    app = Flask(__name__, instance_relative_config=True, instance_path=instance_path)

    # Loading the configuration
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
    
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .controllers.api import index as api_index

    app.register_blueprint(api_index.bp)

    return app