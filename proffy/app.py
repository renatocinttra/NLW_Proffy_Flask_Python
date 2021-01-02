from flask import Flask
from proffy.ext import config


def create_app(app):
    """Factory principal da aplicação"""
    app = Flask(__name__)
    config.init_app(app)

    return app
