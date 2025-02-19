from functools import reduce
from random import shuffle

from blib2to3.pgen2.parse import Results
from flask import Blueprint, render_template, redirect, url_for, session
from flask_login import login_required, current_user
from sqlalchemy import func

from .forms import QuizForm
from ..extensions import db
from ..models import Quiz, Question, Answer, UserResponse, Result, User

quiz_blueprint = Blueprint("quiz", __name__, url_prefix="/quiz")


@quiz_blueprint.route("/start/<id>")
@login_required
def start_quiz(id: int):
    session["quiz_id"] = id
    session["current_question"] = 0
    session["score"] = 0

    # Set the questions in the session
    questions = Question.query.filter_by(quiz_id=id).all()
    shuffle(questions)
    session["questions"] = [question.id for question in questions]
    session["user_responses"] = []
    return redirect(url_for("quiz.quiz"))


@quiz_blueprint.route("/play", methods=["GET", "POST"])
@login_required
def quiz():
    quiz = Quiz.query.filter_by(id=session["quiz_id"]).first()
    form = QuizForm()

    # Fetch the question from DB using the stored ID

    quiz_question_index = session["current_question"]
    current_question_id = session["questions"][quiz_question_index]
    current_question = Question.query.get(current_question_id)
    answers = [(answer.id, answer.text) for answer in current_question.answers]
    form.answer.choices = answers

    if form.validate_on_submit():
        selected_answer_id = form.answer.data
        selected_answer = Answer.query.get(selected_answer_id)

        session["user_responses"].append(
            {
                "user_id": current_user.id,
                "question_id": current_question_id,
                "selected_answer_id": selected_answer_id,
            }
        )

        if selected_answer.is_correct:
            session["score"] += 1

        if session["current_question"] < len(session["questions"]) - 1:
            session["current_question"] += 1
            return redirect(url_for("quiz.quiz"))

        user_responses_db = [
            UserResponse(
                user_id=user_response["user_id"],
                question_id=user_response["question_id"],
                selected_answer_id=user_response["selected_answer_id"],
            )
            for user_response in session["user_responses"]
        ]

        db.session.add_all(user_responses_db)
        db.session.add(
            Result(user_id=current_user.id, quiz_id=quiz.id, score=session["score"])
        )
        db.session.commit()

        # Clean session
        session.pop("current_question")
        session.pop("questions")
        session.pop("quiz_id")
        session.pop("user_responses")
        session.pop("score")

        return redirect(url_for("quiz.leaderboard"))

    return render_template(
        "quiz.html", form=form, total_score=session["score"], question=current_question
    )


@quiz_blueprint.route("/leaderboard")
@login_required
def leaderboard():
    user_scores = (
        db.session.query(Result.user_id, func.sum(Result.score).label("total_score"))
        .group_by(Result.user_id)
        .order_by(func.sum(Result.score).desc())
        .all()
    )

    leaderboard_data = [
        {"username": User.query.get(user_id).username, "score": total_score}
        for user_id, total_score in user_scores
    ]

    return render_template("leaderboard.html", leaderboard=leaderboard_data)
