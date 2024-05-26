from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.Text())
    name = db.Column(db.String(1000))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solution_id = db.Column(db.Integer)
    version = db.Column(db.Text())
    result = db.Column(db.Text())
    reason = db.Column(db.Text())
    confidence = db.Column(db.Integer)
    started_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="questions")


class Practice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solution_id = db.Column(db.Integer)
    version = db.Column(db.Text())
    result = db.Column(db.Text())
    reason = db.Column(db.Text())
    confidence = db.Column(db.Integer)
    started_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="practices")


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    personal_use_1 = db.Column(db.Integer, nullable=False)
    professional_use_2 = db.Column(db.Integer, nullable=False)
    genAI_decisionmaking_3 = db.Column(db.Integer, nullable=False)
    trust_4 = db.Column(db.Integer, nullable=False)
    rationale_5 = db.Column(db.Integer, nullable=False)
    willingness_to_use_6 = db.Column(db.Integer, nullable=False)
    usefulness_7 = db.Column(db.Integer, nullable=False)
    disagree_8 = db.Column(db.Text, nullable=True)
    additional_9 = db.Column(db.Text, nullable=True)
    interview_consent_10 = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    user = db.relationship("User", backref="surveys")
