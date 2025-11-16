# --- Settings ---
# Load environment variables from .env file
set dotenv-load

# --- Variables ---
# Define paths to venv executables.
# This makes all recipes work without you having to `source` anything.
PYTHON := ".venv/bin/python"
PIP    := ".venv/bin/pip"

# --- Project Setup ---

# Create the virtual environment (if it doesn't exist)
@create-venv:
    [ ! -d .venv ] && python3 -m venv .venv || echo "Virtual environment already exists."

# Install/update dependencies from requirements.txt
# Depends on 'create-venv' to ensure it runs first.
@install: create-venv
    {{PIP}} install -r requirements.txt
    @echo "==> Dependencies installed."

# Update/upgrade all packages listed in requirements.txt
@upgrade: create-venv
    {{PIP}} install --upgrade -r requirements.txt
    @echo "==> Dependencies upgraded."

# Remove the venv and __pycache__ directories
@clean:
    rm -rf .venv
    find . -type d -name "__pycache__" -exec rm -rf {} +
    @echo "==> venv and caches cleaned."

# --- Django Development ---

# List available commands
@help:
    just --list

# Run Django development server
@up:
    {{PYTHON}} manage.py runserver

# Create new migrations (now accepts app names, e.g., `just migrations my_app`)
@migrations *args='':
    {{PYTHON}} manage.py makemigrations {{args}}

# Apply migrations
@migrate:
    {{PYTHON}} manage.py migrate

# Run tests
@test *args='':
    {{PYTHON}} manage.py test {{args}}

# Run arbitrary manage.py commands (e.g., `just cmd createsuperuser`)
@cmd *args='':
    {{PYTHON}} manage.py {{args}}