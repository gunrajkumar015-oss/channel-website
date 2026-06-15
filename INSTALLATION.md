# Installation & Setup Guide

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- PostgreSQL (optional, SQLite for development)
- Node.js (optional)
- Docker & Docker Compose (optional)

## Quick Start with Docker

### 1. Clone Repository
```bash
git clone https://github.com/gunrajkumar015-oss/channel-website.git
cd channel-website
```

### 2. Start Services
```bash
docker-compose up -d
```

### 3. Create Superuser
```bash
docker-compose exec backend python manage.py createsuperuser
```

### 4. Access Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

---

## Manual Installation

### Backend Setup

#### 1. Clone Repository
```bash
git clone https://github.com/gunrajkumar015-oss/channel-website.git
cd channel-website/backend
```

#### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Setup Environment Variables
```bash
cd ..
cp .env.example .env
# Edit .env with your configuration
```

#### 5. Database Configuration

**For SQLite (Default):**
No additional setup needed.

**For PostgreSQL:**

1. Install PostgreSQL
2. Create database:
```bash
sudo -u postgres psql
CREATE DATABASE channel_db;
CREATE USER channel_user WITH PASSWORD 'password';
ALTER ROLE channel_user SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE channel_db TO channel_user;
\q
```

3. Update .env:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=channel_db
DB_USER=channel_user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

#### 6. Run Migrations
```bash
cd backend
python manage.py migrate
```

#### 7. Create Superuser
```bash
python manage.py createsuperuser
```

#### 8. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

#### 9. Run Server
```bash
python manage.py runserver
```

Backend available at: http://localhost:8000

---

### Frontend Setup

#### 1. Navigate to Frontend Directory
```bash
cd frontend
```

#### 2. Choose Your Server

**Option 1: Python HTTP Server**
```bash
python -m http.server 8001
```

**Option 2: Node.js HTTP Server**
```bash
npm install -g http-server
http-server -p 8001
```

**Option 3: VS Code Live Server**
- Install Live Server extension
- Right-click index.html → "Open with Live Server"

Frontend available at: http://localhost:8001 (or assigned port)

---

## Environment Variables

Create `.env` file in project root:

```
# Django
DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database - SQLite (Development)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Database - PostgreSQL (Production)
# DB_ENGINE=django.db.backends.postgresql
# DB_NAME=channel_db
# DB_USER=postgres
# DB_PASSWORD=password
# DB_HOST=localhost
# DB_PORT=5432

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Media Files
MEDIA_ROOT=media
MEDIA_URL=/media/

# Email (Optional)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

---

## Troubleshooting

### Port Already in Use

**Django:**
```bash
python manage.py runserver 8001
```

**Frontend:**
```bash
python -m http.server 8002
```

### Database Connection Error

1. Verify PostgreSQL is running
2. Check .env credentials
3. Ensure database exists
4. Check connection parameters

### CORS Errors

Update `CORS_ALLOWED_ORIGINS` in settings.py or .env

### Static Files Not Loading

```bash
python manage.py collectstatic --noinput --clear
```

### Migration Errors

```bash
# Rollback migrations
python manage.py migrate channels_app 0001

# Re-run migrations
python manage.py migrate
```

### Import Errors

```bash
# Verify virtual environment is activated
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

---

## Testing

### Run All Tests
```bash
cd backend
python manage.py test
```

### Run Specific App Tests
```bash
python manage.py test channels_app
```

### Run Specific Test Class
```bash
python manage.py test channels_app.tests.UserTestCase
```

### Run with Coverage
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

---

## Production Deployment

### 1. Environment Setup
```bash
DEBUG=False
SECRET_KEY=generate-strong-secret-key
```

Generate SECRET_KEY:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 2. Configure PostgreSQL

### 3. Setup Static & Media Files
```bash
python manage.py collectstatic --noinput
```

### 4. Configure Web Server

**Gunicorn + Nginx Setup:**

```bash
pip install gunicorn
gunicorn channel_project.wsgi:application --bind 0.0.0.0:8000
```

### 5. SSL/HTTPS

Use Let's Encrypt:
```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d yourdomain.com
```

### 6. Database Backups
```bash
# PostgreSQL backup
pg_dump channel_db > backup.sql

# Restore
psql channel_db < backup.sql
```

---

## Next Steps

1. Read main [README.md](README.md)
2. Explore API documentation
3. Create first channel
4. Upload sample content
5. Test user interactions

---

## Support

For issues:
- Check documentation
- Review troubleshooting section
- Open GitHub issue
- Contact development team
