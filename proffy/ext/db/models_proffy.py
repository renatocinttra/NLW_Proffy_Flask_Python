"""UTF-08"""
# -*- encoding: utf-8 -*-

from proffy.ext.db import db


class Proffys(db.Model):
    """Criação da Tabela Proffy"""
    __tablename__ = "proffys"

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    avatar = db.Column("avatar", db.Unicode)
    whatsapp = db.Column("whatsapp", db.Unicode)
    bio = db.Column("bio", db.Unicode)


class Classes(db.Model):
    """Criação da Tabela Classes"""
    __tablename__ = "classes"

    id = db.Column("id", db.Integer, primary_key=True)
    subject = db.Column("subject", db.Unicode)
    cost = db.Column("cost", db.Unicode)
    proffys_id = db.Column(
        "proffys_id", db.Integer, db.ForeignKey("proffys.id")
    )

    proffys = db.relationship("Proffys", foreign_keys=proffys_id)


class ClassSchedule(db.Model):
    """Criação da Tabela Calendário"""
    __tablename__ = "class_schedule"

    id = db.Column("id", db.Integer, primary_key=True)
    classes_id = db.Column(
        "classes_id", db.Integer, db.ForeignKey("classes.id")
    )
    weekday = db.Column("weekday", db.Integer)
    time_from = db.Column("time_from", db.Integer)
    time_to = db.Column("time_to", db.Integer)

    classes = db.relationship("Classes", foreign_keys=classes_id)
