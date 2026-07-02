# AFRILOTT Website

Django website for AFRILOTT Holding Ltd.

## Local development

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_site_content
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

Create an admin user:

```bash
python manage.py createsuperuser
```

## Deploy on Coolify

This project includes a `Dockerfile` for Coolify. Coolify builds the image, runs migrations, collects static files, and starts Gunicorn.

### 1. Push the code to Git

Push this repository to GitHub, GitLab, or another Git provider connected to Coolify.

### 2. Create a new application in Coolify

1. Open your Coolify dashboard.
2. Create a **New Resource** → **Application**.
3. Choose your Git repository.
4. Set **Build Pack** to **Dockerfile**.
5. Set **Port** to `8000`.
6. Add your domain, for example `https://afrilott.com`.

### 3. Add a PostgreSQL database (recommended)

1. In Coolify, create a **PostgreSQL** database.
2. Link it to your application.
3. Coolify will expose `DATABASE_URL` to the app automatically.

SQLite works for testing, but PostgreSQL is recommended for production.

### 4. Set environment variables

In Coolify → your app → **Environment Variables**, add:

| Variable | Example | Required |
|----------|---------|----------|
| `DEBUG` | `False` | Yes |
| `SECRET_KEY` | long random string | Yes |
| `ALLOWED_HOSTS` | `afrilott.com,www.afrilott.com` | Yes |
| `CSRF_TRUSTED_ORIGINS` | `https://afrilott.com,https://www.afrilott.com` | Yes |
| `DATABASE_URL` | from Coolify PostgreSQL | Recommended |
| `RUN_SEED_ON_STARTUP` | `true` on first deploy only | First deploy |
| `SERVE_MEDIA` | `true` | Yes |
| `GUNICORN_WORKERS` | `2` | Optional |

Generate a secret key locally:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

After the first successful deploy, set `RUN_SEED_ON_STARTUP=false` so content is not re-seeded on every restart.

### 5. Add persistent storage

Uploaded images are stored in `media/`. In Coolify → **Storages**, mount a persistent volume:

| Container path | Purpose |
|----------------|---------|
| `/app/media` | Uploaded images (hero slides, team photos, logos) |

If you use SQLite instead of PostgreSQL, also mount:

| Container path | Purpose |
|----------------|---------|
| `/app/db.sqlite3` | SQLite database file |

### 6. Deploy

Click **Deploy**. On startup the container will:

1. Run `python manage.py migrate`
2. Run `python manage.py collectstatic`
3. Optionally run `python manage.py seed_site_content` if `RUN_SEED_ON_STARTUP=true`
4. Start Gunicorn on port `8000`

### 7. Create an admin user

After the first deploy, open the Coolify app terminal and run:

```bash
python manage.py createsuperuser
```

Then open `https://your-domain.com/admin/`.

### 8. Re-seed content manually (optional)

```bash
python manage.py seed_site_content --reset
```

## Coolify checklist

- [ ] Repository connected
- [ ] Build pack set to Dockerfile
- [ ] Port set to `8000`
- [ ] Domain added with HTTPS
- [ ] `SECRET_KEY`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` set
- [ ] PostgreSQL linked (`DATABASE_URL`)
- [ ] Persistent volume mounted at `/app/media`
- [ ] First deploy with `RUN_SEED_ON_STARTUP=true`
- [ ] Admin user created
- [ ] `RUN_SEED_ON_STARTUP` set back to `false`

## Docker test locally

```bash
docker build -t aflt-website .
docker run --rm -p 8000:8000 ^
  -e DEBUG=False ^
  -e SECRET_KEY=local-test-secret-key-please-change ^
  -e ALLOWED_HOSTS=localhost,127.0.0.1 ^
  -e CSRF_TRUSTED_ORIGINS=http://localhost:8000 ^
  -e RUN_SEED_ON_STARTUP=true ^
  -v aflt-media:/app/media ^
  aflt-website
```

Open `http://127.0.0.1:8000/`.

## Tests

```bash
python manage.py test
```
