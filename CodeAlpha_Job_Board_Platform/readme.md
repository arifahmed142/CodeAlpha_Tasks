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
cd CodeAlpha_Job_Board_Pl
