# Job Board Platform

A Django-powered job portal that connects employers with job seekers through a centralized recruitment platform. Employers can publish and manage job opportunities, while candidates can explore vacancies, submit applications, and track their application progress.

<p align="center">
  <strong>Built with Django · Python · SQLite · Tailwind CSS</strong>
</p>

---

## Overview

The **Job Board Platform** is a web-based recruitment management system designed to simplify the hiring process for both employers and candidates.

The platform provides separate experiences for employers and job seekers. Employers can create job listings, manage their posted opportunities, review applicants, and update application statuses. Candidates can browse available jobs, submit applications with their resumes and relevant information, and monitor their application history.

The project focuses on implementing practical backend development concepts, including custom user authentication, role-based access, database relationships, CRUD operations, file uploads, and server-side request handling.

## Key Features

### Authentication & User Management
- Custom user authentication system.
- Separate candidate and employer account types.
- Email-based authentication.
- Role-based access to platform functionality.
- User profile management.
- Profile photo and document uploads.

### Candidate Features
- Browse available job opportunities.
- View detailed job descriptions and requirements.
- Apply for available positions.
- Upload resumes and provide application information.
- View submitted applications.
- Track application statuses.
- Edit applications while they are pending.

### Employer Features
- Create and publish job vacancies.
- Manage previously posted jobs.
- View all applications received for a job.
- Access individual applicant details.
- Review applicant resumes and cover letters.
- Update application statuses.
- Monitor application activity.

### Application Management
- Store candidate application information.
- Associate applications with specific jobs and candidates.
- Prevent duplicate applications for the same job.
- Maintain application submission and update timestamps.
- Support application statuses:
  - Pending
  - Reviewed
  - Shortlisted
  - Accepted
  - Rejected

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Django | Web framework and application logic |
| SQLite | Relational database |
| HTML5 | Page structure |
| Tailwind CSS | Responsive user interface |
| JavaScript | Client-side interactions |
| Git & GitHub | Version control and project hosting |

## Project Architecture

The application follows Django's modular application structure, separating major responsibilities into dedicated apps.

| Application | Responsibility |
|---|---|
| `Users` | Custom authentication, candidate and employer accounts |
| `Job_Post` | Job creation, listing, editing, and management |
| `Application` | Candidate applications and employer-side applicant management |

### User Architecture

The project uses Django's custom authentication system with `AbstractBaseUser`, `BaseUserManager`, and `PermissionsMixin`.

A shared profile model provides common user information, while separate candidate and employer models extend that profile with role-specific functionality.

### Core Database Relationships

```text
                  profile
                     |
          -----------------------
          |                     |
      candidate              employer
          |                     |
          |                     |
     Application             JobPost
          |                     |
          -----------   ---------
                     |
              Application
```

**Main relationships:**
- A candidate can submit applications to multiple jobs.
- An employer can publish multiple job posts.
- Each application belongs to one candidate and one job.
- Employers can access applications associated with their own job posts.

---

## Installation & Setup

Follow these steps to run the project locally.

### Prerequisites

Make sure you have installed:

- Python 3.10 or later
- Git
- pip (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Navigate to the Project Directory

```bash
cd CodeAlpha_Job_Board_Platform
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

If the repository includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install Django:

```bash
pip install django
```

### 6. Configure Environment Settings

Review the project's settings before running it.

Make sure the custom user model is configured correctly:

```python
AUTH_USER_MODEL = 'Users.profile'
```

Also configure static files and media storage if required.

### 7. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create a Superuser

```bash
python manage.py createsuperuser
```

### 9. Run the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

## Project Structure

The following is a logical overview of the project's Django structure. Actual template and configuration filenames may differ.

```text
CodeAlpha_Job_Board_Platform/
│
├── Users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── Job_Post/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── Application/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│
├── static/
│
├── media/
│
├── manage.py
├── db.sqlite3
└── requirements.txt
```

---

## Application Workflow

### Candidate Workflow

1. Register for a candidate account.
2. Log in to the platform.
3. Browse available job opportunities.
4. Open a job to review its details.
5. Submit an application with personal information and a resume.
6. Visit the My Applications section.
7. Monitor the application status.

### Employer Workflow

1. Register for an employer account.
2. Log in to the platform.
3. Create and publish a job vacancy.
4. Visit the My Posted Jobs section.
5. View applicants for a particular vacancy.
6. Review applicant information and resumes.
7. Update the application status.

---

## Security & Access Control

The platform implements several backend-level access control practices:

- Authentication-protected views.
- Candidate and employer role verification.
- Employer ownership checks for job management.
- Candidate ownership checks for application management.
- CSRF protection for POST requests.
- Password hashing through Django's authentication system.
- Database-level relationships and constraints to maintain data integrity.

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Django custom user models.
- Custom user managers.
- Role-based authentication and authorization.
- Django ORM and relational database relationships.
- CRUD operations.
- ForeignKey and OneToOneField relationships.
- File and image uploads.
- Django template inheritance.
- URL routing and dynamic URL parameters.
- Request handling using GET and POST.
- Application workflow management.
- Git and GitHub project management.

---

## Future Improvements

Potential enhancements for future versions include:

- Advanced job search and filtering.
- Pagination for job listings and applications.
- Email notifications for application updates.
- Employer company profiles.
- Candidate skill-based job recommendations.
- Job bookmarking and saved searches.
- REST API integration using Django REST Framework.
- Automated testing and improved validation.
- Deployment with a production-ready database and hosting environment.

---

## Contribution

Contributions, suggestions, and feedback are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

## Author

**Md. Arif Ahmed**

Backend Development | Python | Django

- GitHub: [My GitHub Profile](https://github.com/arifahmed142)
- LinkedIn: [My LinkedIn Profile]((https://www.linkedin.com/in/arif-ahmed-970147289/)

---

<p align="center">
  If you find this project useful, consider giving it a ⭐ on GitHub.
</p>

<p align="center">
  <strong>Built with Django and a passion for backend development.</strong>
</p>
