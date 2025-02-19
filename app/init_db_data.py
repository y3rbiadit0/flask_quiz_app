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
                        ("Exclusive use of structured data", False),
                        ("Execution of simple arithmetic calculations", False),
                        ("Ability to learn and adapt", True),
                        ("Operation without requiring prior data", False),
                    ],
                },
                {
                    "question": "Which technique is used in deep learning?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.ai,
                    "answers": [
                        ("Genetic algorithms", False),
                        ("Artificial neural networks", True),
                        ("Linear programming", False),
                        ("Decision trees", False),
                    ],
                },
                {
                    "question": "What is the main purpose of reinforcement learning?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.ai,
                    "answers": [
                        ("To create models that predict future values", False),
                        ("To train models to maximize a reward signal", True),
                        ("To analyze unstructured data", False),
                        ("To classify labeled data", False),
                    ],
                },
                {
                    "question": "Which of the following is an example of supervised learning?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.ai,
                    "answers": [
                        ("Clustering data into groups", False),
                        ("Training a model on labeled data", True),
                        ("Analyzing time-series data", False),
                        ("Generating new data from existing data", False),
                    ],
                },
                {
                    "question": "Which AI technique is widely used for classification tasks?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.ai,
                    "answers": [
                        ("Linear regression", False),
                        ("Support vector machines", True),
                        ("K-means clustering", False),
                        ("Principal component analysis", False),
                    ],
                },
            ],
        },
        {
            "quiz": quizzes["computer_vision"],
            "questions": [
                {
                    "question": "Which technique is used to detect edges in an image?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.computer_vision,
                    "answers": [
                        ("Fourier transform", False),
                        ("Canny edge detection", True),
                        ("Image segmentation", False),
                        ("Histographic equalization", False),
                    ],
                },
                {
                    "question": "Which algorithm is used for face recognition in computer vision?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.computer_vision,
                    "answers": [
                        ("K-means clustering", False),
                        ("YOLO", False),
                        ("Haar cascades", True),
                        ("Deep Q-learning", False),
                    ],
                },
                {
                    "question": "Which of the following is NOT typically used for object detection?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.computer_vision,
                    "answers": [
                        ("YOLO", False),
                        ("Faster R-CNN", False),
                        ("SIFT", True),
                        ("SSD", False),
                    ],
                },
                {
                    "question": "Which type of neural network is commonly used for image recognition?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.computer_vision,
                    "answers": [
                        ("Convolutional neural network (CNN)", True),
                        ("Recurrent neural network (RNN)", False),
                        ("Multilayer perceptron (MLP)", False),
                        ("Generative adversarial network (GAN)", False),
                    ],
                },
                {
                    "question": "What is the purpose of image segmentation in computer vision?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.computer_vision,
                    "answers": [
                        ("To reduce image resolution", False),
                        ("To classify objects", False),
                        ("To split an image into meaningful regions", True),
                        ("To filter out noise", False),
                    ],
                },
            ],
        },
        {
            "quiz": quizzes["nlp"],
            "questions": [
                {
                    "question": "Which technique is used to convert words into numerical representations in NLP?",
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
                    "question": "Which of the following is used for sentiment analysis in NLP?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.nlp,
                    "answers": [
                        ("Word2Vec", False),
                        ("SVM (Support Vector Machine)", True),
                        ("BERT", False),
                        ("Hidden Markov Models", False),
                    ],
                },
                {
                    "question": "Which algorithm is commonly used in text classification tasks?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.nlp,
                    "answers": [
                        ("K-means", False),
                        ("Naïve Bayes", True),
                        ("Reinforcement learning", False),
                        ("Q-learning", False),
                    ],
                },
                {
                    "question": "Which of these is an example of a language model?",
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
                    "question": "Which of the following is used for machine translation?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.nlp,
                    "answers": [
                        ("Deep Q-learning", False),
                        ("Seq2Seq models", True),
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
                    "question": "Which Python library is commonly used for AI and machine learning?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.python_ai,
                    "answers": [
                        ("Matplotlib", False),
                        ("TensorFlow", True),
                        ("Flask", False),
                        ("BeautifulSoup", False),
                    ],
                },
                {
                    "question": "Which Python library is popular for data manipulation?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.python_ai,
                    "answers": [
                        ("Django", False),
                        ("Pandas", True),
                        ("TensorFlow", False),
                        ("Scikit-learn", False),
                    ],
                },
                {
                    "question": "Which Python library is used for data visualization?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.python_ai,
                    "answers": [
                        ("Numpy", False),
                        ("Flask", False),
                        ("Matplotlib", True),
                        ("Scipy", False),
                    ],
                },
                {
                    "question": "What does 'PyTorch' specialize in?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.python_ai,
                    "answers": [
                        ("Web development", False),
                        ("Data analysis", False),
                        ("Deep learning", True),
                        ("GUI development", False),
                    ],
                },
                {
                    "question": "Which library is used for natural language processing in Python?",
                    "question_type": QuestionType.multiple_choice,
                    "topic": QuestionTopic.python_ai,
                    "answers": [
                        ("TensorFlow", False),
                        ("NLTK", True),
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
        "ai": Quiz(title="Artificial Intelligence"),
        "computer_vision": Quiz(title="Computer Vision"),
        "nlp": Quiz(title="Natural Language Processing"),
        "python_ai": Quiz(title="Applications of AI Models with Python Applications"),
    }
    db.session.add_all(quizzes.values())
    db.session.commit()
    return quizzes
