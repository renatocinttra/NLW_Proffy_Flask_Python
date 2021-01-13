from flask import render_template, request, url_for, redirect
from flask import Blueprint
from proffy.ext.db.list import proffys, subjects, weekdays
from proffy.ext.site.form import ProffyForm

bp = Blueprint("site", __name__)


@bp.route("/")
def pageLanding():
    return render_template("index.html")


@bp.route("/study", methods=["GET", "POST"])
def pageStudy():
    filters = request.args
    # Try change to loop.index in the conditional of page study.html
    return render_template(
        "study.html",
        proffys=proffys,
        filters=filters,
        subjects=subjects,
        weekdays=weekdays,
    )


@bp.route("/give-classes", methods=["GET", "POST"])
def pageGiveClasses():
    data = request.args
    # Try change to loop.index in the conditional of page give-classes.html
    if len(data) != 0:
        proffys.append(data)
        return redirect(url_for("site.pageStudy"))
    else:
        return render_template(
            "give-classes.html",
            subjects=subjects,
            weekdays=weekdays,
            data=data
        )


@bp.route("/give-classes-test", methods=["GET", "POST"])
def pageGiveClassesTest():
    form = ProffyForm()
    data = request.args
    return render_template(
        "give-classes-test.html",
        form=form,
        subjects=subjects,
        weekdays=weekdays,
        data=data
    )
