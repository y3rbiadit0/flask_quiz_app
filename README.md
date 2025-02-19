# Quiz Application

A Flask-based Quiz Application using `Flask Blueprints`, `Flask-SQLAlchemy`, and `Flask-WTF`.
This application allows users to take quizzes, tracks their scores, and displays a leaderboard.

**By default it uses local SQLite database.

## Features
- User authentication
- Dynamic quiz generation with multiple topics
- Randomized questions and answer choices
- Leaderboard displaying user scores
- Flask Blueprints for modular structure
- Flask-SQLAlchemy for database management
- Flask-WTF for handling forms

## Project Structure
```plaintext
quiz_app/
│── app/
│   │── __init__.py
│   │── auth/ --Authentication related routes.
│   │── home/ --Home Page related routes.
│   │── models/ -- Handle all database models.
│   │── quiz/ -- Quiz related routes.
│   ├── templates/ -- Html templates for rendering.
│   ├── services/ -- To manage business logic at this level.
│   │── extensions.py -- Handle everything related to flask extensions to be used from other parts of the source code.
│   │── app.py -- Initialize Flask App with all the extensions + Config.
│   │── init_db_data.py -- Script that fills the database with initial data.
│── config.py
│── requirements.txt
│── README.md
```

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed.

### Step 1: Clone the Repository
```bash
git clone <repo_url>
cd simple-quiz-app
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
flask run
```

## License
This project is open-source under the MIT License.

