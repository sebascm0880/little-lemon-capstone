# little-lemon-capstone
Capstone project built with Django REST Framework featuring Token Authentication, custom permission logic (IsAdminOrReadOnly), MySQL database integration, and dependency management using uv instead of Pipenv.

# Little Lemon Capstone Project (Django + DRF)

This repository contains a Django REST Framework (DRF) project for the
Little Lemon capstone. It provides endpoints for Menu items and
Bookings, along with token-based authentication.

------------------------------------------------------------------------

## Tech Stack

-   Python 3.12
-   Django
-   Django REST Framework
-   Djoser (user management and token endpoints)
-   MySQL (mysqlclient)
-   uv (dependency management)

------------------------------------------------------------------------

## Dependency Management (uv instead of Pipenv)

This project uses **uv** for dependency management instead of Pipenv.

Key files: - `pyproject.toml` → project dependencies - `uv.lock` →
locked dependency resolution for reproducible installs

### Install dependencies

1.  Install uv (follow official instructions for your OS).

2.  From the project root:

    uv sync

3.  Run Django commands using uv:

    uv run python manage.py migrate uv run python manage.py runserver

Note: Pipenv is not used in this project.

------------------------------------------------------------------------

## Database Configuration (MySQL)

The project is configured to use MySQL in `LittleLemon/settings.py`.

Before running migrations:

1.  Create a MySQL database named `LittleLemon`.
2.  Update database credentials in `settings.py` if necessary.

Security Recommendation: Database credentials are currently defined
directly in `settings.py` for development purposes. For production
environments, credentials should be stored in environment variables.

------------------------------------------------------------------------

## Running Migrations

    uv run python manage.py makemigrations
    uv run python manage.py migrate

------------------------------------------------------------------------

## Authentication

This project supports Token Authentication via DRF and Djoser.

### DRF Token Endpoint

POST /restaurant/api-token-auth/

Example:

curl -X POST http://127.0.0.1:8000/restaurant/api-token-auth/\
-H "Content-Type: application/json"\
-d "{\"username\":\"YOUR_USER\",\"password\":\"YOUR_PASSWORD\"}"

### Djoser Endpoints

-   POST /auth/token/login/
-   POST /auth/token/logout/
-   User management endpoints under /auth/

------------------------------------------------------------------------

## API Endpoints

Base path: /restaurant/

### Menu

-   GET /restaurant/menu/
-   POST /restaurant/menu/
-   GET /restaurant/menu/`<id>`{=html}/
-   PUT /restaurant/menu/`<id>`{=html}/
-   PATCH /restaurant/menu/`<id>`{=html}/
-   DELETE /restaurant/menu/`<id>`{=html}/

### Bookings

-   GET /restaurant/bookings/
-   POST /restaurant/bookings/
-   GET /restaurant/bookings/`<id>`{=html}/
-   PUT /restaurant/bookings/`<id>`{=html}/
-   PATCH /restaurant/bookings/`<id>`{=html}/
-   DELETE /restaurant/bookings/`<id>`{=html}/

------------------------------------------------------------------------

## Permissions

### Menu (Custom Permission Added as Plus)

A custom permission class `IsAdminOrReadOnly` was implemented for Menu
endpoints.

Behavior: - Read-only methods (GET, HEAD, OPTIONS) are allowed for any
request. - Write methods (POST, PUT, PATCH, DELETE) require: - An
authenticated user, and - Membership in the Django Group named
`Manager`.

Applied in: - `MenuItemView` - `SingleMenuItemView`

### Bookings

Bookings use:

    permission_classes = [IsAuthenticated]

Meaning: Any authenticated user with a valid token can perform CRUD
operations on Bookings.

------------------------------------------------------------------------

## Development Notes

-   DEBUG=True is enabled for local development only.
-   ALLOWED_HOSTS is empty for local use.
-   For production, move secrets to environment variables and disable
    DEBUG.

