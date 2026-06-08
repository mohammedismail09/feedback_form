# Feedback Form Project

A simple and robust Django web application designed to collect user feedback through a web form, store the entries securely in a database, and manage them via the built-in Django Admin interface.

---

## 🚀 Features & Development Steps

1. **Virtual Environment Isolation**: Keeps project dependencies clean and separate.
2. **Django Framework**: Built using Python's most popular high-level web framework.
3. **Modular Architecture**: Project structural configuration separated from application logic.
4. **Data Modeling**: Structural database design mapped natively using Django ORM.
5. **Django Forms API**: Automated form generation, styling hooks, and server-side validation.
6. **Persistent Storage**: Secure SQL database storage for all submitted feedback.
7. **Admin Dashboard**: Built-in, secure control panel to read, filter, and delete user feedback.

---

## 🛠️ Installation & Setup Instructions

Follow these steps to get the development environment running locally.

### 1. Clone the Project & Navigate
```bash
cd C:\Users\Rehaan\Desktop\feedback_form
```

### 2. Create and Activate Virtual Environment
```bash
# Create the environment
python -m venv venv

# Activate on Windows (Command Prompt)
venv\Scripts\activate

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Apply Database Migrations
Generate and execute the database schema based on the feedback models:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an Admin User (Superuser)
To access the data inside the admin panel, create a management account:
```bash
python manage.py createsuperuser
```
*Follow the on-screen prompts to set a username, email, and password.*

### 6. Run the Development Server
```bash
python manage.py runserver
```
* Open your browser and navigate to `http://127.0.0` to view the form.
* Navigate to `http://127.0.0admin/` to log into the management dashboard.

---

## 📂 Project Architecture Reference

```text
feedback_form/                <-- Root Directory
│── feedback_form/            <-- Project Configuration Directory
│   ├── settings.py           <-- Global Settings
│   ├── urls.py               <-- Root URL Routing
│   └── wsgi.py / asgi.py     <-- Server Deployment Gateways
│── [your_app_name]/          <-- Application Directory
│   ├── models.py             <-- Database Schema Definitions
│   ├── forms.py              <-- Form Layout and Validation
│   ├── views.py              <-- Request handling logic
│   └── admin.py              <-- Admin Panel Registration
│── venv/                     <-- Isolated Python Environment (Ignored by Git)
│── db.sqlite3                <-- Local Database (Ignored by Git)
└── manage.py                 <-- Django Command Line Utility
```
