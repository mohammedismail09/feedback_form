# Feedback Form Project

A simple and robust Django web application designed to collect user feedback through a web form, store the entries securely in a database, and manage them via the built-in Django Admin interface. This project is fully containerized using Docker for seamless development and deployment.

---

## 🚀 Features & Development Steps

1. **Virtual Environment Isolation**: Keeps project dependencies clean and separate for local usage.
2. **Django Framework**: Built using Python's most popular high-level web framework.
3. **Modular Architecture**: Project structural configuration separated from application logic.
4. **Data Modeling**: Structural database design mapped natively using Django ORM.
5. **Django Forms API**: Automated form generation, styling hooks, and server-side validation.
6. **Persistent Storage**: Secure SQL database storage for all submitted feedback.
7. **Admin Dashboard**: Built-in, secure control panel to read, filter, and delete user feedback.
8. **Docker Containerization**: Entire app environment packaged into a Docker container for consistent running across any system.

---

## 🐳 Docker Setup & Execution (Recommended)

Make sure you have [Docker Desktop](https://docker.com) installed and running on your system.

### 1. Build the Docker Image
Navigate to your project root folder and build the container image:
```bash
docker build -t feedback-form-app .
```

### 2. Run the Container
Launch the container and map it to your local port 8000:
```bash
docker run -p 8000:8000 feedback-form-app
```
* Open your browser and navigate to `http://127.0.0` to view the application.

---

## 🛠️ Local Installation & Setup Instructions (Without Docker)

If you prefer to run the development environment natively on your machine, follow these steps.

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
│── Dockerfile                <-- Docker Configuration Instructions
│── requirements.txt          <-- Python Package Dependencies List
└── manage.py                 <-- Django Command Line Utility
```
