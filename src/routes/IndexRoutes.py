# Imports
from flask import Blueprint, jsonify
from uuid import uuid4
import os

# Random Generator
from src.utils.RandomGenerator import RandomGenerator


main = Blueprint('index_blueprint', __name__)


@main.route('/')
def index():
    json_body = {
        'env_variable': os.getenv('ENVIRONMENT', 'Development'),
        'id': uuid4(),
        'name': RandomGenerator.generate_name(),
        'password': RandomGenerator.generate_password()
    }

    return jsonify(json_body)
