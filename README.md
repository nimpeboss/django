# StudyBuddy

A lightweight Django application for tracking study subjects and timed study sessions.

## Features

- Track subjects and associate study sessions with users
- Record session duration and date
- Simple dashboard and subject management UI

## Getting started

Prerequisites:
- Python 3.11+ (or compatible)
- A virtual environment (recommended)

Installation:

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Visit `/` for the home page
- Visit `/dashboard/` to view your study sessions (login required)
- Visit `/add_subject/` to add new subjects

## Contributing

Contributions are welcome. Please open issues for bugs or feature requests and submit pull requests for fixes or improvements.

> Note: This project is actively maintained but receives informal updates when the developer has spare time (or, as the developer puts it, "when bored").

## License

See the `LICENSE` file for license details.
