import os

from flask import Blueprint, render_template
from flask_login import login_required, current_user
import pandas as pd

from . import db

main = Blueprint("main", __name__)

csv_path = os.path.join(os.path.dirname(__file__), "static/csv/solutions.csv")
df = pd.read_csv(csv_path)


@main.route("/")
def index():
    return render_template("index.html.j2")


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html.j2", name=current_user.name)


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html.j2", name=current_user.name)


@main.route("/solutions")
@login_required
def index_solutions():
    df['title'] = df['Provide a one-line summary of your solution.'].astype(str).apply(lambda x: x[:100])
    solutions = df.to_dict(orient="records")
    return render_template(
        "solutions_index.html.j2",
        solutions=solutions,
    )


@main.route("/solutions/<int:id>/v1")
@login_required
def show_solutions_v1(id):
    df.drop(
        columns=[
            "Advance",
            "Pass_1",
            "FailReason_1",
            "Pass_2",
            "FailReason_2",
        ],
        inplace=True,
        errors="ignore",
    )
    solutions = df[df["Solution ID"] == id].to_dict(orient="records")
    if not solutions:
        return "Solution not found", 404
    return render_template("solutions_show_v1.html.j2", id=id, solution=solutions[0])


@main.route("/solutions/<int:id>/v2")
@login_required
def show_solutions_v2(id):
    return render_template("solutions_show_v2.html.j2", id=id)


@main.route("/solutions/<int:id>/v3")
@login_required
def show_solutions_v3(id):
    return render_template("solutions_show_v3.html.j2", id=id)
