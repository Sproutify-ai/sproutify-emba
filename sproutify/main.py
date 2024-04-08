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
    d = df.copy()
    d["title"] = (
        d["Provide a one-line summary of your solution."]
        .astype(str)
        .apply(lambda x: x[:100])
    )
    solutions = d.to_dict(orient="records")
    return render_template(
        "solutions_index.html.j2",
        solutions=solutions,
    )


@main.route("/solutions/<int:id>/v1")
@login_required
def show_solutions_v1(id):
    d = df.copy()
    solution = d[d["Solution ID"] == id].iloc[0]
    if solution.empty:
        return "Solution not found", 404

    tags = d[["Solution ID", "Challenge Name", "Solution Status"]].to_dict(
        orient="records"
    )[0]
    solution.drop(
        [
            "Advance",
            "Pass_1",
            "FailReason_1",
            "Pass_2",
            "FailReason_2",
            "Solution ID",
            "Challenge Name",
            "Solution Status",
        ],
        inplace=True,
        errors="ignore",
    )

    criteria = {
        "Is the solution application complete, appropriate, and intelligible?": "",
        "Is the solution at least in Prototype stage?": "",
        "Does the solution address the Challenge question?": "",
        "Is the solution powered by technology?": "",
        "The quality of the solution is good enough that an external reviewer should take the time to read and score it": "",
    }

    return render_template(
        "solutions_show_v1.html.j2",
        id=id,
        solution=solution.to_dict(),
        tags=tags,
        criteria=criteria,
    )


@main.route("/solutions/<int:id>/v2")
@login_required
def show_solutions_v2(id):
    d = df.copy()
    solution = d[d["Solution ID"] == id].iloc[0]
    if solution.empty:
        return "Solution not found", 404

    tags = d[["Solution ID", "Challenge Name", "Solution Status"]].to_dict(
        orient="records"
    )[0]
    solution.drop(
        [
            "Advance",
            "Pass_1",
            "FailReason_1",
            "Pass_2",
            "FailReason_2",
            "Solution ID",
            "Challenge Name",
            "Solution Status",
        ],
        inplace=True,
        errors="ignore",
    )

    criteria = {
        "Is the solution application complete, appropriate, and intelligible?": {
            "is_passed": True,
            "reason": "",
        },
        "Is the solution at least in Prototype stage?": {
            "is_passed": True,
            "reason": "",
        },
        "Does the solution address the Challenge question?": {
            "is_passed": False,
            "reason": "reason1",
        },
        "Is the solution powered by technology?": {
            "is_passed": False,
            "reason": "reason2",
        },
        "The quality of the solution is good enough that an external reviewer should take the time to read and score it": {
            "is_passed": True,
            "reason": "",
        },
    }

    return render_template(
        "solutions_show_v2.html.j2",
        id=id,
        solution=solution.to_dict(),
        tags=tags,
        criteria=criteria,
    )

@main.route("/solutions/<int:id>/v3")
@login_required
def show_solutions_v3(id):
    d = df.copy()
    solution = d[d["Solution ID"] == id].iloc[0]
    if solution.empty:
        return "Solution not found", 404

    tags = d[["Solution ID", "Challenge Name", "Solution Status"]].to_dict(
        orient="records"
    )[0]
    solution.drop(
        [
            "Advance",
            "Pass_1",
            "FailReason_1",
            "Pass_2",
            "FailReason_2",
            "Solution ID",
            "Challenge Name",
            "Solution Status",
        ],
        inplace=True,
        errors="ignore",
    )

    criteria = {
        "Is the solution application complete, appropriate, and intelligible?": "summary1",
        "Is the solution at least in Prototype stage?": "summary2",
        "Does the solution address the Challenge question?": "summary3",
        "Is the solution powered by technology?": "summary4",
        "The quality of the solution is good enough that an external reviewer should take the time to read and score it": "summary5",
    }

    return render_template(
        "solutions_show_v3.html.j2",
        id=id,
        solution=solution.to_dict(),
        tags=tags,
        criteria=criteria,
    )