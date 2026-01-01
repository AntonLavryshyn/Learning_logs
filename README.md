# Learning Logs

One of my first applications written in pure Django.  
This app allows users to keep a register of interesting topics and make notes on them, helping to organize study progress in a clean and minimal interface.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Screenshots](#screenshots)
- [License](#license)

---

## Overview

Learning Logs is a Django web application that helps users:

- Track their learning topics
- Add entries for each topic
- Keep personal notes
- Organize learning progress with a clean interface

---

## Features

- User registration and login/logout  
- Create, edit, and delete topics  
- Add entries under each topic  
- Responsive design using Bootstrap 4  
- Simple and minimal interface

---

## Getting Started

Follow these steps to run the project locally:

### Prerequisites

- Python 3.x ([Download Python](https://www.python.org/))  
- pip (Python package manager)  
- Optional: virtual environment (`venv`)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/AntonLavryshyn/Learning_logs.git
Navigate to the project folder:

bash
Копіювати код
cd Learning_logs
Create and activate a virtual environment:

Windows:

bash
Копіювати код
python -m venv env
env\Scripts\activate
macOS/Linux:

bash
Копіювати код
python -m venv env
source env/bin/activate
Install dependencies:

bash
Копіювати код
pip install -r requirements.txt
Apply database migrations:

bash
Копіювати код
python manage.py migrate
Run the development server:

bash
Копіювати код
python manage.py runserver
Open your browser at http://127.0.0.1:8000/

Usage
Register a new user

Log in

Add topics for your learning goals

Add entries under each topic

Edit or delete topics and entries as needed

Technologies
Python 3.x

Django 4.x

Bootstrap 4

SQLite (default database)
