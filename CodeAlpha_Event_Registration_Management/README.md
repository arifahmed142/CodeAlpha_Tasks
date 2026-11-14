# Event Registration Management System

A Django-based web application designed to provide a structured platform for managing users and event-related activities. The project focuses on user authentication, profile management, and administrative user management through a clean web interface.

## Overview

The **Event Registration Management System** is developed using Python and Django. It follows a modular application structure to keep different functionalities organized and maintainable.

The project includes a custom user authentication system, profile management, and administrative features that allow authorized users to manage and search registered members.

## Features

### User Authentication
- User registration using email and password.
- Custom Django user model.
- Secure password storage using Django authentication.
- User login and logout functionality.
- Superuser and regular-user role management.

### User Profile Management
- View personal profile information.
- Upload and manage profile photos.
- Update account information.
- Change account password.
- Delete user account with confirmation.

### Administrative Management
- Superuser-only member management.
- View registered members.
- Search members by name, email, or phone number.
- Separate administrative access from regular user access.

### User Interface
- Django template-based frontend.
- Tailwind CSS for styling.
- Reusable templates and shared layout components.
- Static and media file management.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| SQLite | Database |
| HTML5 | Webpage structure |
| CSS3 | Styling |
| Tailwind CSS | Responsive UI styling |
| JavaScript | Frontend interactions |
| Git & GitHub | Version control |

## Project Structure

```text
Event_Registration_Management/
│
├── Event_Registration_Management/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── Event_Accounts/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── Event_HomePage/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── urls.py
│
├── media/
├── static/
├── manage.py
└── db.sqlite3
```

*Note: The structure above represents the main project components. Your actual folders may contain additional files.*

## Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/USERNAME/Event_Registration_Management.git
```

### 2. Navigate to the Project Directory

```bash
cd Event_Registration_Management
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install django pillow
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the terminal instructions to create your administrator account. 

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Configuration

Before running the project, make sure the following settings are configured correctly in `settings.py`:

```python
AUTH_USER_MODEL = 'Event_Accounts.CustomUser'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
```

For local development, ensure that your media files are served correctly when `DEBUG = True`.

## Authentication and Authorization

The project uses Django's built-in authentication system with a custom user model.

- Regular users can access their own account and profile features.
- Superusers have access to administrative member management.
- Passwords are handled through Django's secure password-hashing mechanism.
- Login-protected views restrict access to authenticated users.

## Future Improvements

Potential improvements for future versions include:

- Complete event creation and management functionality.
- Event registration and cancellation.
- Event capacity and availability management.
- Email notifications and registration confirmations.
- Advanced event search and filtering.
- REST API integration using Django REST Framework.
- Automated testing and improved validation.
- Deployment to a production server.

## Security Notes

- Do not commit secret keys, passwords, or sensitive environment variables.
- Do not upload a production database containing private user information.
- Configure `DEBUG = False` before production deployment.
- Use environment variables for sensitive configuration.
- Configure proper allowed hosts and production static/media file handling.

## Contribution

Contributions, suggestions, and improvements are welcome.

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Submit a pull request.
---

**Developed as a Django-based web development project.**
