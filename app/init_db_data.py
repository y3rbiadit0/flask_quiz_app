from typing import Dict

import flask_sqlalchemy

from .extensions import bcrypt
from .models import (
    Quiz,
    Question,
    QuestionType,
    QuestionTopic,
    User,
    Answer,
    Result,
    UserResponse,
)

"""This script is only to pre-initialize DB with some data"""


def init_db(db: flask_sqlalchemy.SQLAlchemy):
    _clean_database(db)
    _create_admin_user(db)
    quizzes = _create_quizzes(db)
    _create_questions(db, quizzes)


def _clean_database(db: flask_sqlalchemy.SQLAlchemy):
    db.session.query(Answer).delete()
    db.session.query(Question).delete()
    db.session.query(Quiz).delete()
    db.session.query(User).delete()
    db.session.query(Result).delete()
    db.session.query(UserResponse).delete()
    db.session.commit()


def _create_admin_user(db: flask_sqlalchemy.SQLAlchemy):
    first_user = User(
        username="admin", password_hash=bcrypt.generate_password_hash("admin123")
    )
    db.session.add(first_user)
    db.session.commit()


def _create_questions(db: flask_sqlalchemy.SQLAlchemy, quizzes: Dict[str, Quiz]):
    questions_data = [
        {
            "quiz": quizzes["ai"],
            "questions": [
                {
                    "question": "Which of the following is a key feature of artificial intelligence?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.ai,
                    "answers": [
                        ("Ability to learn and adapt", True),
                        ("Exclusive use of structured data", False),
                        ("Can only perform basic math calculations", False),
                        ("Requires no prior data", False),
                    ],
                },
                {
                    "question": "Which technique is commonly used in deep learning?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.ai,
                    "answers": [
                        ("Artificial neural networks", True),
                        ("Genetic algorithms", False),
                        ("Linear programming", False),
                        ("Decision trees", False),
                    ],
                },
                {
                    "question": "What is the main purpose of reinforcement learning?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.ai,
                    "answers": [
                        ("To train models to maximize a reward signal", True),
                        ("To create models that predict future values", False),
                        ("To analyze unstructured data", False),
                        ("To classify labeled data", False),
                    ],
                },
                {
                    "question": "Which of the following is an example of supervised learning?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.ai,
                    "answers": [
                        ("Training a model on labeled data", True),
                        ("Clustering data into groups", False),
                        ("Analyzing time-series data", False),
                        ("Generating new data from existing data", False),
                    ],
                },
                {
                    "question": "Which AI technique is used in many apps for face recognition?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.ai,
                    "answers": [
                        ("Support vector machines", False),
                        ("Linear regression", False),
                        ("K-means clustering", False),
                        ("Convolutional neural networks (CNN)", True),
                    ],
                },
            ],
        },
        {
            "quiz": quizzes["computer_vision"],
            "questions": [
                {
                    "question": "Which technique is used to find edges in an image?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.computer_vision,
                    "answers": [
                        ("Canny edge detection", True),
                        ("Fourier transform", False),
                        ("Image segmentation", False),
                        ("Histographic equalization", False),
                    ],
                },
                {
                    "question": "Which algorithm is used to recognize faces in photos?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.computer_vision,
                    "answers": [
                        ("Haar cascades", True),
                        ("K-means clustering", False),
                        ("YOLO", False),
                        ("Deep Q-learning", False),
                    ],
                },
                {
                    "question": "Which of these is NOT commonly used for detecting objects in pictures?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.computer_vision,
                    "answers": [
                        ("SIFT", True),
                        ("YOLO", False),
                        ("Faster R-CNN", False),
                        ("SSD", False),
                    ],
                },
                {
                    "question": "Which type of neural network is used for image recognition?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.computer_vision,
                    "answers": [
                        ("Convolutional neural network (CNN)", True),
                        ("Recurrent neural network (RNN)", False),
                        ("Generative adversarial network (GAN)", False),
                        ("Multilayer perceptron (MLP)", False),
                    ],
                },
                {
                    "question": "What is the purpose of splitting an image into smaller parts in computer vision?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.computer_vision,
                    "answers": [
                        ("To split an image into meaningful regions", True),
                        ("To filter out noise", False),
                        ("To classify objects", False),
                        ("To reduce image resolution", False),
                    ],
                },
            ],
        },
        {
            "quiz": quizzes["nlp"],
            "questions": [
                {
                    "question": "Which technique is used to convert words into numbers in NLP?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.nlp,
                    "answers": [
                        ("Word embeddings", True),
                        ("Naïve Bayes", False),
                        ("TF-IDF", False),
                        ("LDA", False),
                    ],
                },
                {
                    "question": "Which of these is used for understanding emotions in text (sentiment analysis)?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.nlp,
                    "answers": [
                        ("SVM (Support Vector Machine)", True),
                        ("Word2Vec", False),
                        ("BERT", False),
                        ("Hidden Markov Models", False),
                    ],
                },
                {
                    "question": "Which algorithm is used for categorizing text into topics?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.nlp,
                    "answers": [
                        ("Naïve Bayes", True),
                        ("K-means", False),
                        ("Reinforcement learning", False),
                        ("Q-learning", False),
                    ],
                },
                {
                    "question": "Which of these is a language model that can generate text?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.nlp,
                    "answers": [
                        ("GPT-3", True),
                        ("Decision tree", False),
                        ("K-means clustering", False),
                        ("VGG-16", False),
                    ],
                },
                {
                    "question": "Which of the following is used for translating text between languages?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.nlp,
                    "answers": [
                        ("Seq2Seq models", True),
                        ("Deep Q-learning", False),
                        ("K-means clustering", False),
                        ("Gaussian Naive Bayes", False),
                    ],
                },
            ],
        },
        {
            "quiz": quizzes["python_ai"],
            "questions": [
                {
                    "question": "Which Python library is widely used for AI and machine learning?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.python_ai,
                    "answers": [
                        ("TensorFlow", True),
                        ("Matplotlib", False),
                        ("Flask", False),
                        ("BeautifulSoup", False),
                    ],
                },
                {
                    "question": "Which Python library helps with organizing and analyzing data?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.python_ai,
                    "answers": [
                        ("Pandas", True),
                        ("Django", False),
                        ("TensorFlow", False),
                        ("Scikit-learn", False),
                    ],
                },
                {
                    "question": "Which Python library is used for drawing charts and graphs?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.python_ai,
                    "answers": [
                        ("Matplotlib", True),
                        ("Flask", False),
                        ("Numpy", False),
                        ("Scipy", False),
                    ],
                },
                {
                    "question": "What does 'PyTorch' specialize in?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.python_ai,
                    "answers": [
                        ("Deep learning", True),
                        ("Data analysis", False),
                        ("Web development", False),
                        ("GUI development", False),
                    ],
                },
                {
                    "question": "Which library is used for working with text in Python?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.python_ai,
                    "answers": [
                        ("NLTK", True),
                        ("TensorFlow", False),
                        ("Keras", False),
                        ("OpenCV", False),
                    ],
                },
            ],
        },
    ]
    for quiz_data in questions_data:
        for q_data in quiz_data["questions"]:
            question = Question(
                quiz_id=quiz_data["quiz"].id,
                question=q_data["question"],
                question_type=q_data["question_type"].value,
                topic=q_data["topic"],
            )
            db.session.add(question)
            db.session.commit()

            for answer_text, is_correct in q_data["answers"]:
                answer = Answer(
                    question_id=question.id, text=answer_text, is_correct=is_correct
                )
                db.session.add(answer)
    db.session.commit()


def _create_quizzes(db: flask_sqlalchemy.SQLAlchemy) -> Dict[str, Quiz]:
    quizzes = {
        "ai": Quiz(title="Artificial Intelligence for Beginners"),
        "computer_vision": Quiz(title="Introduction to Computer Vision"),
        "nlp": Quiz(title="Basics of Natural Language Processing"),
        "python_ai": Quiz(title="Python for AI and Machine Learning"),
    }
    db.session.add_all(quizzes.values())
    db.session.commit()
    return quizzes
