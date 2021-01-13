""" Módulo de inicilização do DebugToolbar """
from flask_debugtoolbar import DebugToolbarExtension


def init_app(app):
    """ Inicilizando objeto DebugToolbar na Aplicação """
    if app.debug:
        DebugToolbarExtension(app)
