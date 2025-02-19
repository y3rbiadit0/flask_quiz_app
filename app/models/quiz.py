from datetime import datetime
from enum import Enum

from ..extensions import db


class QuestionType(Enum):
    multiple_choice = "multiple_choice"
    true_false = "true_false"
    short_answer = "short_answer"


class QuestionTopic(Enum):
    ai = "Artificial Intelligence"
    computer_vision = "Computer Vision"
    nlp = "Natural Language Processing"
    python_ai = "Applications of AI Models with Python Applications"


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quiz.id"), nullable=False)

    question = db.Column(db.String(350), unique=True)
    question_type = db.Column(db.String(50), nullable=False)
    answers = db.relationship("Answer", backref="question", lazy=True)
    topic = db.Column(db.Enum(QuestionTopic), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)


class UserResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    selected_answer_id = db.Column(
        db.Integer, db.ForeignKey("answer.id"), nullable=True
    )
    responded_at = db.Column(db.DateTime, default=datetime.now())


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    questions = db.relationship("Question", backref="quiz", lazy=True)


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quiz.id"), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    taken_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return "<Question: {}>".format(self.question)
