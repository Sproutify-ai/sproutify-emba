import os
import random

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import pandas as pd
import json

from . import db
from .models import Question, Practice, Survey

main = Blueprint("main", __name__)

# assessment version
csv_path = os.path.join(
    os.path.dirname(__file__), "static/csv/Updated_Criteria_With_Selected_vf.csv"
)

# practice version
practice_path = os.path.join(os.path.dirname(__file__), "static/csv/sample_5_2023.csv")

num_practice = 2
total_num_questions = 10
num_questions_split = 2

drop_cols = [
    "Solution ID",
    "Challenge Name",
    "Solution Status",
    "Advance",
    "Pass_1",
    "FailReason_1",
    "Pass_2",
    "FailReason_2",
    "Solution ID",
    "Challenge Name",
    "Solution Status",
    "gpt_full_result",
    "gpt_full_advance",
    "gpt_selected_result",
    "gpt_selected_advance",
    "gpt_summary_result",
    "gpt_summary_advance",
    "summary",
]
df = pd.read_csv(csv_path)
df = df[df["Selected"] == 1]
practice_df = pd.read_csv(practice_path)


def parse_criteria(selected_results, version):
    base_criteria = {
        "Criterion 1 - Is the solution application complete, appropriate, and intelligible?": {},
        "Criterion 2 - Is the solution at least in Prototype stage?": {},
        "Criterion 3 - Does the solution address the Challenge question?": {},
        "Criterion 4 - Is the solution powered by technology?": {},
        "Criterion 5 - The quality of the solution is good enough that an external reviewer should take the time to read and score it": {},
    }

    if version == "v1":
        return {key: "" for key in base_criteria.keys()}

    for key, criteria in selected_results.items():
        criterion_key = {
            "criteria_1": "Criterion 1 - Is the solution application complete, appropriate, and intelligible?",
            "criteria_2": "Criterion 2 - Is the solution at least in Prototype stage?",
            "criteria_3": "Criterion 3 - Does the solution address the Challenge question?",
            "criteria_4": "Criterion 4 - Is the solution powered by technology?",
            "criteria_5": "Criterion 5 - The quality of the solution is good enough that an external reviewer should take the time to read and score it",
        }.get(key)

        is_passed = criteria["result"]
        base_criteria[criterion_key] = {
            "is_passed": is_passed,
            "reason": (
                f"""<span class="has-text-weight-semibold">Reason:</span> <span>{criteria['reason']}<span>"""
                if version == "v3"
                else ""
            ),
        }

    return base_criteria


def show_solutions_generic(id, version, is_practice=False):
    d = practice_df if is_practice else df
    solution = d[d["Solution ID"] == id]
    if solution.empty:
        return "Solution not found", 404

    tags = solution[["Name", "Solution ID", "Challenge Name"]].to_dict(
        orient="records"
    )[0]

    # selected_results = json.loads(solution['hd_selected_result'].iloc[0])

    solution_all = (
        solution.iloc[:, 2:42].to_dict(orient="records")[0]
        if not solution.empty
        else {}
    )
    solution_c2 = (
        solution.iloc[:, [13, 14, 9, 34, 10]].to_dict(orient="records")[0]
        if not solution.empty
        else {}
    )
    solution_c3 = (
        solution.iloc[:, [8, 7, 9, 11]].to_dict(orient="records")[0]
        if not solution.empty
        else {}
    )
    solution_c4 = (
        solution.iloc[:, [8, 26, 29, 32]].to_dict(orient="records")[0]
        if not solution.empty
        else {}
    )
    summary = (
        solution["summary"].iloc[0]
        if "summary" in solution.columns
        else "No summary available."
    )

    # criteria = parse_criteria(selected_results, version)

    criteria_names = {
        "criteria_1": "Criterion 1 - Is the solution application complete, appropriate, and intelligible?",
        "criteria_2": "Criterion 2 - Is the solution at least in Prototype stage?",
        "criteria_3": "Criterion 3 - Does the solution address the Challenge question?",
        "criteria_4": "Criterion 4 - Is the solution powered by technology?",
        "criteria_5": "Criterion 5 - The quality of the solution is good enough that an external reviewer should take the time to read and score it",
    }
    criteria = {}
    s = solution.iloc[0].to_dict()
    reason_format = (
        """<span class="has-text-weight-semibold">Reason:</span> <span>{}<span>"""
    )
    criteria[criteria_names["criteria_1"]] = {}
    criteria[criteria_names["criteria_1"]]["is_passed"] = s["Pass Criterion1"]
    criteria[criteria_names["criteria_1"]]["reason"] = reason_format.format(
        s["Rationale Criterion 1"]
    )
    criteria[criteria_names["criteria_2"]] = {}
    criteria[criteria_names["criteria_2"]]["is_passed"] = s["Pass Criterion2"]
    criteria[criteria_names["criteria_2"]]["reason"] = reason_format.format(
        s["Rationale Criterion 2"]
    )
    criteria[criteria_names["criteria_3"]] = {}
    criteria[criteria_names["criteria_3"]]["is_passed"] = s["Pass Criterion3"]
    criteria[criteria_names["criteria_3"]]["reason"] = reason_format.format(
        s["Rationale Criterion 3"]
    )
    criteria[criteria_names["criteria_4"]] = {}
    criteria[criteria_names["criteria_4"]]["is_passed"] = s["Pass Criterion4"]
    criteria[criteria_names["criteria_4"]]["reason"] = reason_format.format(
        s["Rationale Criterion 4"]
    )
    criteria[criteria_names["criteria_5"]] = {}
    criteria[criteria_names["criteria_5"]]["is_passed"] = s["Pass Criterion5"]
    criteria[criteria_names["criteria_5"]]["reason"] = reason_format.format(
        s["Rationale Criterion 5"]
    )

    is_pass = False
    if version in ["v2", "v3"]:
        is_pass = all([criteria[key]["is_passed"] for key in criteria.keys()])

    if not is_practice:
        total_solutions = total_num_questions
        num_questions = (
            total_solutions
            + 1
            - Question.query.filter_by(user_id=current_user.id, result=None).count()
        )
    else:
        total_solutions = num_practice
        num_questions = (
            total_solutions
            + 1
            - Practice.query.filter_by(user_id=current_user.id, result=None).count()
        )

    return render_template(
        "solutions_show.html",
        id=id,
        solution_all=solution_all,
        solution_c2=solution_c2,
        solution_c3=solution_c3,
        solution_c4=solution_c4,
        solution_summary=summary,
        tags=tags,
        criteria=criteria,
        is_pass=is_pass,
        is_practice=is_practice,
        total_solutions=total_solutions,
        solution_count=num_questions,
    )


@main.context_processor
def cache_busters():
    return {
        "tooltips": [
            "Use the failure reason associated with criteria 1 if the application is not in English, provides only a few words for required questions, is not intelligible (for e.g., if you can’t figure out what the solution is after reading the application), or if the application was clearly created to offend/isn’t taking the Challenge seriously.",
            "Prototype stage means that the venture or organization is building and testing its product, service, or business model. Use the failure reason associated with criteria 2 if no concrete product, service, or business model is being built yet.",
            "Use the failure reason associated with criteria 3 if the solution does not address the broad Challenge question. (It’s acceptable if it addresses the Challenge generally, even if it does not address one of the dimensions specifically.).",
            "Every Solve solution must include technology, whether new / existing or high-tech / low-tech. Ask yourself: If you removed the tech component of this solution, would the solution still work? If your answer to this question is “yes,” then the solution does not pass this criterion.",
            "This is subjective, but think about whether it would be a waste of time / embarrassing for Solve if an external Reviewer was asked to read this solution and score it along the Review Criteria. Do not pass the solution on this criterion if you think it would be a waste of an external Reviewer’s time. Another indication that it’s not worth the Reviewer’s time: after reading the application, you don’t know what the solution is.",
        ],
    }


@main.route("/")
def index():
    return redirect(url_for("main.instructions"))


@main.route("/test")
def test():
    return render_template("test.html")


@main.route("/practice")
def practice():
    tbl = Practice

    # If the user already completed more than num_questions, redirect to complete page
    if (
        tbl.query.filter(tbl.user_id == current_user.id, tbl.result != None).count()
        >= num_practice
    ):
        return redirect(url_for("main.practice_complete"))

    if tbl.query.filter(tbl.user_id == current_user.id, tbl.result != None).count() > 0:
        last_question = tbl.query.filter_by(
            user_id=current_user.id, result=None
        ).first()
        return redirect(
            url_for(
                "main.show_solutions_%s" % last_question.version,
                id=last_question.solution_id,
                is_practice=True,
            )
        )

    if tbl.query.filter(tbl.user_id == current_user.id).count() > 0:
        last_question = tbl.query.filter_by(user_id=current_user.id).first()
        return redirect(
            url_for(
                "main.show_solutions_%s" % last_question.version,
                id=last_question.solution_id,
                is_practice=True,
            )
        )

    random_rows = practice_df["Solution ID"].to_list()[:num_practice]
    versions = ["v1", "v1"]
    version1 = random.choice(versions)

    print(random_rows, version1)
    for row in random_rows[:num_practice]:
        question = tbl(
            user_id=current_user.id,
            solution_id=row,
            version=version1,
        )
        db.session.add(question)
        db.session.commit()

    first_id = random_rows[0]
    question = tbl.query.filter_by(solution_id=first_id).first()
    question.started_at = db.func.now()
    db.session.commit()
    return redirect(
        url_for("main.show_solutions_%s" % version1, id=first_id, is_practice=True)
    )


@main.route("/start")
def start():
    tbl_p = Practice

    # Check if the user already completed practice
    if (
        tbl_p.query.filter(
            tbl_p.user_id == current_user.id, tbl_p.result != None
        ).count()
        >= num_practice
    ):
        tbl_s = Survey
        tbl = Question
        # Check if the user already completed survey
        if (
            tbl_s.query.filter(
                tbl_s.user_id == current_user.id, tbl_s.updated_at != None
            ).count()
            > 0
        ):
            return redirect(url_for("main.complete"))
        # Check if the user already completed 20 questions
        elif (
            tbl.query.filter(tbl.user_id == current_user.id, tbl.result != None).count()
            >= total_num_questions
        ):
            return redirect(url_for("main.survey"))

        if (
            tbl.query.filter(tbl.user_id == current_user.id, tbl.result != None).count()
            > 0
        ):
            last_question = tbl.query.filter_by(
                user_id=current_user.id, result=None
            ).first()
            return redirect(
                url_for(
                    "main.show_solutions_%s" % last_question.version,
                    id=last_question.solution_id,
                )
            )

        if tbl.query.filter(tbl.user_id == current_user.id).count() > 0:
            last_question = tbl.query.filter_by(user_id=current_user.id).first()
            return redirect(
                url_for(
                    "main.show_solutions_%s" % last_question.version,
                    id=last_question.solution_id,
                )
            )

        random_rows = df.sample(n=total_num_questions)["Solution ID"].to_list()
        versions = ["v1", "v2", "v3"]
        version1 = random.choice(versions)
        versions.pop(versions.index(version1))
        version2 = random.choice(versions)

        print(random_rows, version1, version2)
        for row in random_rows[:num_questions_split]:
            question = tbl(
                user_id=current_user.id,
                solution_id=row,
                version=version1,
            )
            db.session.add(question)
            db.session.commit()
        for row in random_rows[num_questions_split:]:
            question = tbl(
                user_id=current_user.id,
                solution_id=row,
                version=version2,
            )
            db.session.add(question)
            db.session.commit()

        first_id = random_rows[0]
        question = tbl.query.filter_by(solution_id=first_id).first()
        question.started_at = db.func.now()
        db.session.commit()
        return redirect(url_for("main.show_solutions_%s" % version1, id=first_id))
    else:
        return render_template("no_practice.html", num_practice=num_practice)


@main.route("/instructions")
@login_required
def instructions():
    return render_template("instructions.html", name=current_user.name)


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", name=current_user.name)


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
        "solutions_index.html",
        solutions=solutions,
    )


@main.route("/solutions/<int:id>/98q3hiwnaj")
@login_required
def show_solutions_v1(id):
    is_practice = request.args.get("is_practice")
    return show_solutions_generic(id, "v1", is_practice=is_practice)


@main.route("/solutions/<int:id>/98hy3fqeh3")
@login_required
def show_solutions_v2(id):
    is_practice = request.args.get("is_practice")
    return show_solutions_generic(id, "v2", is_practice=is_practice)


@main.route("/solutions/<int:id>/0o3e8u5t8i")
@login_required
def show_solutions_v3(id):
    is_practice = request.args.get("is_practice")
    return show_solutions_generic(id, "v3", is_practice=is_practice)


@main.route("/complete")
@login_required
def complete():
    return render_template("complete.html")


@main.route("/practice_complete")
@login_required
def practice_complete():
    return render_template("practice_complete.html")


@main.route("/record", methods=["POST"])
@login_required
def record():
    form = request.form
    is_practice = form.get("is_practice")
    solution_id = form.get("solution_id")
    result = form.get("result")
    reason = form.get("reason")
    confidence = form.get("confidence")

    print(form, is_practice, solution_id, result, reason, confidence)

    tbl = Question
    if is_practice:
        tbl = Practice

    question = tbl.query.filter_by(
        solution_id=solution_id, user_id=current_user.id
    ).first()
    question.result = result
    question.reason = reason
    question.confidence = confidence
    question.completed_at = db.func.now()
    db.session.commit()

    next_question = tbl.query.filter_by(user_id=current_user.id, result=None).first()

    if next_question:
        next_question.started_at = db.func.now()
        db.session.commit()
        return redirect(
            url_for(
                "main.show_solutions_%s" % next_question.version,
                id=next_question.solution_id,
                is_practice=is_practice,
            )
        )
    else:
        if is_practice:
            return redirect(url_for("main.practice_complete"))
        return redirect(url_for("main.survey"))


@main.route("/survey", methods=["GET", "POST"])
@login_required
def survey():
    if request.method == "POST":
        page = int(request.form.get("page"))

        if page == 1:
            personal_use = request.form.get("personal_use")
            professional_use = request.form.get("professional_use")
            genAI_decisionmaking = request.form.get("genAI_decisionmaking")
            return render_template(
                "survey.html",
                page=2,
                personal_use=personal_use,
                professional_use=professional_use,
                genAI_decisionmaking=genAI_decisionmaking,
            )
        elif page == 2:
            personal_use = request.form.get("personal_use")
            professional_use = request.form.get("professional_use")
            genAI_decisionmaking = request.form.get("genAI_decisionmaking")
            trust = request.form.get("trust")
            rationale = request.form.get("rationale")
            willingness_to_use = request.form.get("willingness_to_use")
            usefulness = request.form.get("usefulness")
            disagree = request.form.get("disagree")
            additional = request.form.get("additional")

            return render_template(
                "survey.html",
                page=3,
                personal_use=personal_use,
                professional_use=professional_use,
                genAI_decisionmaking=genAI_decisionmaking,
                trust=trust,
                rationale=rationale,
                willingness_to_use=willingness_to_use,
                usefulness=usefulness,
                disagree=disagree,
                additional=additional,
            )
        elif page == 3:
            personal_use = request.form.get("personal_use")
            professional_use = request.form.get("professional_use")
            genAI_decisionmaking = request.form.get("genAI_decisionmaking")
            trust = request.form.get("trust")
            rationale = request.form.get("rationale")
            willingness_to_use = request.form.get("willingness_to_use")
            usefulness = request.form.get("usefulness")
            disagree = request.form.get("disagree")
            additional = request.form.get("additional")
            interview_consent = request.form.get("interview_consent")

            survey_response = Survey(
                user_id=current_user.id,
                personal_use_1=personal_use,
                professional_use_2=professional_use,
                genAI_decisionmaking_3=genAI_decisionmaking,
                trust_4=trust,
                rationale_5=rationale,
                willingness_to_use_6=willingness_to_use,
                usefulness_7=usefulness,
                disagree_8=disagree,
                additional_9=additional,
                interview_consent_10=interview_consent,
            )
            db.session.add(survey_response)
            db.session.commit()
            return redirect(url_for("main.complete"))

    return render_template("survey.html", page=1)
