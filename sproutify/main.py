import os

from flask import Blueprint, render_template
from flask_login import login_required, current_user
import pandas as pd

from . import db

main = Blueprint("main", __name__)

csv_path = os.path.join(os.path.dirname(__file__), "static/csv/solutions.csv")
df = pd.read_csv(csv_path)

@main.context_processor
def cache_busters():
    return {
        "tooltips": [
            "Use the failure reason associated with criteria 1 if the application is not in English, provides only a few words for required questions, is not intelligible (for e.g., if you can’t figure out what the solution is after reading the application), or if the application was clearly created to offend/isn’t taking the Challenge seriously.",
            "Prototype stage means that the venture or organization is building and testing its product, service, or business model. Use the failure reason associated with criteria 2 if no concrete product, service, or business model is being built yet.",
            "Use the failure reason associated with criteria 3 if the solution does not address the broad Challenge question. (It’s acceptable if it addresses the Challenge generally, even if it does not address one of the dimensions specifically.).",
            'Every Solve solution must include technology, whether new / existing or high-tech / low-tech. Ask yourself: If you removed the tech component of this solution, would the solution still work? If your answer to this question is “yes,” then the solution does not pass this criterion.',
            'This is subjective, but think about whether it would be a waste of time / embarrassing for Solve if an external Reviewer was asked to read this solution and score it along the Review Criteria. Do not pass the solution on this criterion if you think it would be a waste of an external Reviewer’s time. Another indication that it’s not worth the Reviewer’s time: after reading the application, you don’t know what the solution is.',
        ],
    }

@main.route("/")
def index():
    return render_template("index.html.j2")


@main.route("/test")
def test():
    return render_template("test.html.j2")


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

    tags = d[["Solution ID", "Challenge Name"]].to_dict(
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
        "Is the solution application complete, appropriate, and intelligible?": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
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

    tags = d[["Solution ID", "Challenge Name"]].to_dict(
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
        "C1: Is the solution application complete, appropriate, and intelligible?": {
            "is_passed": True,
            "reason": "",
        },
        "C2: Is the solution at least in Prototype stage?": {
            "is_passed": True,
            "reason": "",
        },
        "C3: Does the solution address the Challenge question?": {
            "is_passed": False,
            "reason": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        },
        "C4: Is the solution powered by technology?": {
            "is_passed": False,
            "reason": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        },
        "C5: The quality of the solution is good enough that an external reviewer should take the time to read and score it": {
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

    tags = d[["Solution ID", "Challenge Name"]].to_dict(
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
        "C1: Is the solution application complete, appropriate, and intelligible?": {
            "is_passed": True,
            "reason": "Reason: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        },
        "C2: Is the solution at least in Prototype stage?": {
            "is_passed": True,
            "reason": "Reason: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        },
        "C3: Does the solution address the Challenge question?": {
            "is_passed": False,
            "reason": "Reason: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        },
        "C4: Is the solution powered by technology?": {
            "is_passed": False,
            "reason": "Reason: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        },
        "C5: The quality of the solution is good enough that an external reviewer should take the time to read and score it": {
            "is_passed": True,
            "reason": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        },
    }

    return render_template(
        "solutions_show_v3.html.j2",
        id=id,
        solution=solution.to_dict(),
        tags=tags,
        criteria=criteria,
    )