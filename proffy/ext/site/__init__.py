from .main import bp

"""Importando a instancia de bp do arquivo Main"""


def init_app(app):
    """Iniciando o Blueprint"""
    app.register_blueprint(bp)
