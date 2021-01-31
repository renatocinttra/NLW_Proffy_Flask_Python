"""Importando a bliblioteca WTForms"""
import wtforms as wtf
import wtforms.fields.html5 as wtf5
from flask_wtf import FlaskForm
from markupsafe import Markup
from proffy.ext.db.list import subjects, weekdays


class ProffyForm(FlaskForm):
    """Criando o formulário a partir de uma classe"""
    name = wtf.StringField(
        "Nome Completo",
        [wtf.validators.DataRequired()]
    )
    avatar = wtf5.URLField(
        Markup("Link da sua foto <small>(comece com https://)</small>"),
        [wtf.validators.DataRequired()]
    )
    whatsapp = wtf5.TelField(
        Markup("Whatsapp <small>(somente número)</small>"),
        [wtf.validators.DataRequired()]
    )
    bio = wtf.TextAreaField(
        "Biografia",
        [wtf.validators.DataRequired()]
    )
    subject = wtf.SelectField(
        u"Matéria",
        [wtf.validators.DataRequired()],
        choices=subjects,
        # TODO: O valor default passa pelo validators, corrigir o problema posteriormente.
        default=0
    )
    cost = wtf5.DecimalField(
        Markup("Custo da sua hora/aula<small>(R$)</small>"),
        [wtf.validators.DataRequired()]
    )
    weekday = wtf.SelectField(
        u"Dia da Semana",
        [wtf.validators.DataRequired()],
        choices=weekdays,
        # O valor default passa pelo validators, corrigir o problema posteriormente.
        default=0
    )
    time_from = wtf5.TimeField(
        "Das",
        [wtf.validators.DataRequired()]
    )
    time_to = wtf5.TimeField(
        "Até",
        [wtf.validators.DataRequired()]
    )
    button = wtf.SubmitField("Salvar Cadastro")
