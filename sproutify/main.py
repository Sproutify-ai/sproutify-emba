import os

from flask import Blueprint, render_template
from flask_login import login_required, current_user
import pandas as pd
import json

from . import db

main = Blueprint("main", __name__)

csv_path = os.path.join(os.path.dirname(__file__), "static/csv/t.csv")
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
            "summary"]
df = pd.read_csv(csv_path)

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
            "criteria_5": "Criterion 5 - The quality of the solution is good enough that an external reviewer should take the time to read and score it"
        }.get(key)
        
        is_passed = criteria['result']
        base_criteria[criterion_key] = {
            "is_passed": is_passed,
            "reason": f'''<span class="has-text-weight-semibold">Reason:</span> <span>{criteria['reason']}<span>''' if version == "v3" else ""
        }
    
    return base_criteria

def show_solutions_generic(id, version):
    d = df.copy()
    solution = d[d["Solution ID"] == id]
    if solution.empty:
        return "Solution not found", 404
    
    tags = solution[["Name", "Solution ID", "Challenge Name"]].to_dict(
        orient="records"
    )[0]

    #selected_results = json.loads(solution['hd_selected_result'].iloc[0])

    solution_all = solution.iloc[:, 2:42].to_dict(orient="records")[0] if not solution.empty else {}
    solution_c2 = solution.iloc[:, [13, 14, 9, 34, 10]].to_dict(orient="records")[0] if not solution.empty else {}
    solution_c3 = solution.iloc[:, [8, 7, 9, 11]].to_dict(orient="records")[0] if not solution.empty else {}
    solution_c4 = solution.iloc[:, [8, 26, 29, 32]].to_dict(orient="records")[0] if not solution.empty else {}
    summary = solution['summary'].iloc[0] if 'summary' in solution.columns else "No summary available."

    #criteria = parse_criteria(selected_results, version)

    criteria_names = {
        "criteria_1": "Criterion 1 - Is the solution application complete, appropriate, and intelligible?",
        "criteria_2": "Criterion 2 - Is the solution at least in Prototype stage?",
        "criteria_3": "Criterion 3 - Does the solution address the Challenge question?",
        "criteria_4": "Criterion 4 - Is the solution powered by technology?",
        "criteria_5": "Criterion 5 - The quality of the solution is good enough that an external reviewer should take the time to read and score it",
    }
    criteria = {}
    s = solution.iloc[0].to_dict()
    reason_format = '''<span class="has-text-weight-semibold">Reason:</span> <span>{}<span>'''
    criteria[criteria_names['criteria_1']] = {}
    criteria[criteria_names['criteria_1']]['is_passed'] = s['Pass Criterion1']
    criteria[criteria_names['criteria_1']]['reason'] = reason_format.format(s['Rationale Criterion 1'])
    criteria[criteria_names['criteria_2']] = {}
    criteria[criteria_names['criteria_2']]['is_passed'] = s['Pass Criterion2']
    criteria[criteria_names['criteria_2']]['reason'] = reason_format.format(s['Rationale Criterion 2'])
    criteria[criteria_names['criteria_3']] = {}
    criteria[criteria_names['criteria_3']]['is_passed'] = s['Pass Criterion3']
    criteria[criteria_names['criteria_3']]['reason'] = reason_format.format(s['Rationale Criterion 3'])
    criteria[criteria_names['criteria_4']] = {}
    criteria[criteria_names['criteria_4']]['is_passed'] = s['Pass Criterion4']
    criteria[criteria_names['criteria_4']]['reason'] = reason_format.format(s['Rationale Criterion 4'])
    criteria[criteria_names['criteria_5']] = {}
    criteria[criteria_names['criteria_5']]['is_passed'] = s['Pass Criterion5']
    criteria[criteria_names['criteria_5']]['reason'] = reason_format.format(s['Rationale Criterion 5'])

    is_pass = False
    if version in ["v2", "v3"]:
        is_pass = all([criteria[key]['is_passed'] for key in criteria.keys()])

    return render_template(
        "solutions_show.html.j2",
        id=id, 
        solution_all=solution_all, 
        solution_c2=solution_c2, 
        solution_c3=solution_c3, 
        solution_c4=solution_c4, 
        solution_summary=summary,
        tags=tags,
        criteria=criteria,
        is_pass=is_pass,
    )

def show_complete():
    return render_template(
        "complete.html.j2"
    )

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


@main.route("/solutions/<int:id>/98q3hiwnaj")
@login_required
def show_solutions_v1(id):
    return show_solutions_generic(id, "v1")

@main.route("/solutions/<int:id>/98hy3fqeh3")
@login_required
def show_solutions_v2(id):
    return show_solutions_generic(id, "v2")

@main.route("/solutions/<int:id>/0o3e8u5t8i")
@login_required
def show_solutions_v3(id):
    return show_solutions_generic(id, "v3")

@main.route("/complete")
@login_required
def complete():
    return show_complete()
