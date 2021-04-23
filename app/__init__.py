import logging

from flask import Flask

from .cli import app_cli
from .blueprints import api_v1

# =============================================================================
# Factory function for Flask
# =============================================================================

def create_app():
    app = Flask(__name__)

    # Setup logging
    if app.env == 'development':
        app.logger.setLevel(logging.DEBUG)
    else:
        app.logger.setLevel(logging.ERROR)

    # NOTE: SECTION:CONFIG: Set your config values here

    # NOTE: SECTION:EXTENSIONS: Initialize your extensions here

    # NOTE: SECTION:BLUEPRINTS: Register your blueprints here
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    # NOTE: SECTION:CLI: Register your commands and AppGroup's here
    app.cli.add_command(app_cli)

    return app
