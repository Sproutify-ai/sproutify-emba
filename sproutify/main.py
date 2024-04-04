import os

from flask import Blueprint, render_template
from flask_login import login_required, current_user
import pandas as pd

from . import db

main = Blueprint("main", __name__)

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
    csv_path = os.path.join(os.path.dirname(__file__), 'static/csv/solutions.csv')
    df = pd.read_csv(csv_path)
    return render_template("solutions_index.html.j2", titles=df['Provide a one-line summary of your solution.'])

@main.route("/solutions/<id>")
@login_required
def show_solutions(id):
    return render_template("solutions_show.html.j2", id=id)