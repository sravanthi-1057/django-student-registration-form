# Django Student Registration

A simple Django project for student registration.

## Features

- Student registration form
- Store student details in database
- Django admin panel
- HTML templates
- SQLite database

## Technologies Used

- Python
- Django
- HTML
- SQLite

## Project Structure

studentproject/
│
├── studentapp/
├── studentproject/
├── templates/
│   └── studentapp/
│       ├── register.html
│       └── success.html
├── manage.py

## Run Project

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Virtual Environment

```bash
source venv/bin/activate
```

### Install Django

```bash
pip install django
```

### Run Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Start Server

```bash
python3 manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

## Author

Abhinaya
