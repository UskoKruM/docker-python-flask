# Imports
from flask import Flask
from flask_cors import CORS

# Consts
from .utils.consts import ALLOWED_ORIGINS

# Middlewares
from .routes.middlewares.ErrorMiddleware import ErrorMiddleware

# Routes
from .routes import IndexRoutes


app = Flask(__name__)

CORS(app, origins=[ALLOWED_ORIGINS])


@app.errorhandler(Exception)
def handle_exception(ex):
    return ErrorMiddleware.handle_error_500(ex)


def init_app(config: dict = None):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')

    # Error Handlers
    app.register_error_handler(401, ErrorMiddleware.handle_error_401)

    return app
