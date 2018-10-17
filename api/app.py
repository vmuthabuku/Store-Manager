from flask import Flask
from ..instance.config import app_config
from .v1.endpoints.product_endpoints import product_print


def create_app(config):
    """Receives the necessary configuration and passes to create_app"""

    app = Flask(__name__)
    app.config.from_object(app_config[config])
    app.url_map.strict_slashes = False

    app.register_blueprint(product_print)   

    return app

