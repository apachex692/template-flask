# Author: Sakthi Santhosh
# Created on: 30/12/2023
from flask import Flask


def create_app():
    app_handler = Flask(__name__)

    return app_handler
