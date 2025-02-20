# Quiz Application
 
A Flask-based Quiz Application using `Flask Blueprints`, `Flask-SQLAlchemy`, `Flask-Login`, and `Flask-WTF`.
This application allows users to take quizzes, tracks their scores, and displays a leaderboard.

*_By default it uses local SQLite database._

-> *Hosted in [PythonAnywhere](https://www.pythonanywhere.com/)*: [Simple Quiz Application](https://merendafrancon.eu.pythonanywhere.com/) 
## Features
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - User authentication 
- Dynamic quiz generation with multiple topics
- Randomized questions and answer choices
- Leaderboard displaying user scores
- [Flask Blueprints](https://flask.palletsprojects.com/en/stable/blueprints/) for modular structure
- [Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/) for database management
- [Flask-WTF](https://flask.palletsprojects.com/en/stable/patterns/wtforms/) for handling forms

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

### Room for improvement:
1. UI/UX - To make it more fun
2. Move the logic from controllers to the `service` to handle it properly
3. For `services` - at the time of consuming an API, add a Client and split responsabilities.
4. Add `tests`
