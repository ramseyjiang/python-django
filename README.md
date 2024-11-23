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
Ensure you have the following installed: Docker and Docker Compose

2. Clone the Repository
   ```
   git clone <repository_url>
   cd myproject
   ```
3. Build and Run the Docker Containers
   ```
   docker-compose up --build
   ```
4. Run Database Migrations
   Once the containers are running, apply the migrations:
   ```
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```
5. Create a Superuser (Optional)
   To access the Django admin:
   ```
   docker-compose exec web python manage.py createsuperuser
   ```
   
6. Access the Application
   
   	•	The application will be available at: http://localhost:8000
	•	Django Admin: http://localhost:8000/admin

  ## **Database Configuration**  
  The project uses PostgreSQL, configured in docker-compose.yml. Default credentials are:
  ```
POSTGRES_DB: myproject
POSTGRES_USER: myuser
POSTGRES_PASSWORD: mypassword
```

You can change these in the docker-compose.yml file and the corresponding settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

## **Project Structure Explanation**
1. Django App Structure (web/)
---
	•	Models (models.py):
	•	Author, Publisher, Book models are defined for database interaction.
	•	Views (views.py):
	•	CRUD functionality is implemented for Books, Authors, and Publishers.
	•	Templates (templates/):
	•	HTML templates for each entity.
	•	Includes Bootstrap styling for responsiveness.
---
2. Docker Configuration
---
	•	Dockerfile: Builds a container for the Django app.
	•	docker-compose.yml: Orchestrates the web (Django app) and db (PostgreSQL) containers.
---


## **Commands**
Run the Application
```
docker-compose up
```

Stop the Containers
```
docker-compose down
```

Rebuild the Containers
```
docker-compose build --no-cache
```

Run Migrations
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

Rebuild the Tests
```
docker-compose exec web python manage.py test web.tests
```

[![Coverage Status](https://coveralls.io/repos/github/username/repository/badge.svg?branch=main)](https://coveralls.io/github/username/repository?branch=main)
