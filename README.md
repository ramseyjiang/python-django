# **Django CRUD Application with Docker**

This project is a Django-based web application for managing **Books**, **Authors**, and **Publishers** with full CRUD functionality. It uses Docker for containerized deployment, PostgreSQL as the database, and Bootstrap for styling.

---

## **Project Structure**

```plaintext
myproject/                # Project Root
├── localenv/             # Local Python virtual environment (ignored in Docker)
├── myproject/            # Django project folder
│   ├── __init__.py       # Project initialization file
│   ├── asgi.py           # ASGI application
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # WSGI application
├── web/                  # Django app folder
│   ├── migrations/       # Database migrations
│   ├── static/           # Static files (CSS, JS, etc.)
│   ├── templates/        # HTML templates
│   │   ├── books/        # Templates for Books CRUD
│   │   ├── authors/      # Templates for Authors CRUD
│   │   ├── publishers/   # Templates for Publishers CRUD
│   ├── admin.py          # Admin interface
│   ├── apps.py           # App configuration
│   ├── models.py         # Database models
│   ├── views.py          # Views (CRUD operations)
│   ├── urls.py           # App-specific URL routing
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Dockerfile for building the Django app
├── db.sqlite3            # SQLite database (only for local use)
```


## **Features**
	•	CRUD Operations for managing:
	•	Books (Title, Author, Publisher, Price, Publication Date)
	•	Authors (Name)
	•	Publishers (Name)
	•	Styled using Bootstrap 5.3 for responsive design.
	•	Uses PostgreSQL as the database.

 ## **Setup and Installation**
 1. Prerequisites
	Ensure you have the following installed:
	•	Docker
	•	Docker Compose

2. Clone the Repository
   ```git clone <repository_url>
   cd myproject
