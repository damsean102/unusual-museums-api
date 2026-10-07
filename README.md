# Unusual Museums API

A small Flask API that serves museum data from a Google Sheet.

## Requirements

Before getting started, make sure you have:

- Python 3.14 or later
- [`uv`](https://docs.astral.sh/uv/)
- Access to the Google service account credentials used by the project

## Install `uv`

On macOS:

```bash
brew install uv
```

## Project setup

Clone the repository and move into it:

```bash
git clone <repository-url>
cd unusual-museums-api
```

Install the project dependencies:

```bash
uv sync
```

This will create a local `.venv` automatically and install the dependencies defined in `pyproject.toml`.

## Google credentials

The API reads its museum data from a Google Sheet using a Google service account.

Create a `.env` file in the project root:

```bash
touch .env
```

Add the path to your Google service account credentials:

```env
GOOGLE_APPLICATION_CREDENTIALS=./app/google-credentials.json
```

The value should point to a valid Google service account JSON credentials file.

For example:

```text
unusual-museums-api/
├── app/
│   └── google-credentials.json
├── static/
├── .env
├── app.py
├── pyproject.toml
└── uv.lock
```

The service account must have access to the Google Sheet named:

```text
Museums
```

Do not commit the `.env` file or Google service account credentials to Git.

## Run locally

Run the application using:

```bash
uv run python app.py
```

The development server should start on:

```text
http://127.0.0.1:5000
```

You can then access the API at:

```text
http://127.0.0.1:5000/api/
```

### Run with Flask

You can also use the Flask development server:

```bash
uv run flask --app app run --debug
```

### Run with Gunicorn

To run the application in a way that more closely matches production:

```bash
uv run gunicorn app:app
```

Gunicorn will listen on:

```text
http://127.0.0.1:8000
```

## API endpoints

### List all museums

```http
GET /api/
```

Example:

```bash
curl http://127.0.0.1:5000/api/
```

Returns all museums from the configured Google Sheet.

### Get a museum

```http
GET /api/<id>
```

For example:

```bash
curl http://127.0.0.1:5000/api/0
```

Returns the museum at the specified index.

If the supplied ID is not numeric, the API returns a `422 Unprocessable Entity` response.

## Managing dependencies

Add a new dependency:

```bash
uv add <package>
```

For example:

```bash
uv add requests
```

Remove a dependency:

```bash
uv remove <package>
```

Update all dependencies to the newest versions allowed by `pyproject.toml`:

```bash
uv lock --upgrade
uv sync
```

Check the installed dependency tree:

```bash
uv tree
```

## Production

The project uses Gunicorn in production.

The Heroku `Procfile` contains:

```text
web: gunicorn app:app
```

This tells Gunicorn to load the `app` Flask application from `app.py`.
