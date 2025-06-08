# Django Sum API

A minimal Django project that exposes a simple API to add two numbers via POST request.

---

## Features

- Accepts JSON input via POST: `{"x": 10, "y": 5}`
- Returns the sum as JSON: `{"sum": 15}`

---

## How to Run

```bash
# 1. Clone the project
git clone https://github.com/your-username/django-learning.git
cd django-learning

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install django

# 4. Run the server
python manage.py runserver
