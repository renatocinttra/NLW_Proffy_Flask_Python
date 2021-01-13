"""Criando comandos no Flask"""
import click
from proffy.ext.db import db
from proffy.ext.db import models_proffy


def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()

    @app.cli.command()
    def list_proffys():
        # TODO: usar tabulate
        click.echo("Lista de Professores")
