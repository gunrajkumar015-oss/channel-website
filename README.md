# Channel Website - Full Stack Platform

A modern, responsive, full-featured channel platform built with Django, where users can be readers or writers. Upload videos, images, articles, and engage through comments with advanced features like trending content and channel recommendations.

## Features

### User Management
- Two user types: Readers and Writers
- User authentication and profiles
- Role-based permissions
- User follow system

### Content Management
- **Videos**: Upload, stream, and manage video content
- **Images**: Gallery management with image uploads
- **Articles**: Rich text article creation and publishing
- **Comments**: Threaded comments with timestamps, usernames, and ratings

### Advanced Features
- Like/dislike system
- Trending content dashboard
- Channel subscriptions
- Search functionality
- User recommendations
- Admin panel for content moderation

## Technology Stack

**Backend:**
- Django 4.2+
- Django REST Framework
- PostgreSQL/SQLite
- Celery for async tasks
- Pillow for image processing
- django-cors-headers
- python-decouple for environment variables

**Frontend:**
- HTML5, CSS3, JavaScript (Vanilla + jQuery)
- Bootstrap 5 for responsive design
- Responsive video player
- Modern image gallery
- Real-time comments

## Project Structure

```
channel-website/
├── backend/
│   ├── channel_project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── channels_app/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── media/
│   ├── static/
│   ├── templates/
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── pages/
├── docker-compose.yml
├── .env.example
└── README.md
```

## Quick Start

### Prerequisites
- Python 3.8+
- pip
- PostgreSQL (optional, SQLite for development)
- Docker (optional)

### With Docker

```bash
git clone https://github.com/gunrajkumar015-oss/channel-website.git
cd channel-website

docker-compose up -d
```

Access:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Admin: http://localhost:8000/admin

### Manual Setup

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

cp ../.env.example .env

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend API: http://localhost:8000

#### Frontend

```bash
cd frontend
python -m http.server 8001
```

Frontend: http://localhost:8001

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login user
- `POST /api/auth/logout/` - Logout user
- `GET /api/auth/profile/` - Get user profile

### Channels
- `GET /api/channels/` - List all channels
- `POST /api/channels/` - Create channel (writers only)
- `GET /api/channels/<id>/` - Get channel details
- `POST /api/channels/<id>/subscribe/` - Subscribe to channel

### Videos
- `GET /api/videos/` - List videos
- `POST /api/videos/` - Upload video (writers only)
- `GET /api/videos/<id>/` - Get video details

### Articles
- `GET /api/articles/` - List articles
- `POST /api/articles/` - Create article (writers only)
- `GET /api/articles/<id>/` - Get article details

### Comments
- `GET /api/comments/` - List comments
- `POST /api/comments/` - Create comment
- `GET /api/comments/?video=<id>` - Get video comments

### Images
- `GET /api/images/` - List images
- `POST /api/images/` - Upload image

### Likes
- `POST /api/likes/` - Like content

### Notifications
- `GET /api/notifications/` - Get user notifications
- `POST /api/notifications/mark_all_as_read/` - Mark as read

## User Roles

### Reader
- Browse channels and content
- Watch videos
- Read articles
- View galleries
- Like and comment
- Subscribe to channels

### Writer
- Create and manage channels
- Upload videos
- Publish articles
- Upload images
- Manage comments
- View analytics

## Database Models

### Core Models
- **User** - Django built-in user model
- **UserProfile** - Extended user info (type, bio, picture)
- **Channel** - Content channel
- **Follow** - User following relationships
- **Subscription** - Channel subscriptions

### Content Models
- **Video** - Video content with metadata
- **Article** - Article/blog post content
- **Image** - Image gallery items

### Engagement Models
- **Comment** - Comments on content
- **Like** - Likes on content and comments
- **Notification** - User notifications

## Docker Support

The project includes Docker configuration for easy deployment:

```bash
docker-compose up -d      # Start all services
docker-compose down       # Stop all services
docker-compose logs -f    # View logs
```

Services:
- PostgreSQL database
- Redis cache
- Django backend
- Nginx frontend

## Configuration

### Environment Variables

Create `.env` file from `.env.example`:

```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

For PostgreSQL:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=channel_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

## Features in Detail

### User Authentication
- Secure registration and login
- Role-based access control
- User profiles with customization
- Password reset functionality

### Content Management
- Video upload with thumbnail generation
- Article editor with rich text support
- Image gallery with organization
- Content publication workflow

### Engagement System
- Like/dislike on any content
- Comment threads with nesting
- User mentions in comments
- Like notifications

### Discovery
- Trending content
- Channel recommendations
- Search functionality
- Category browsing

### Analytics
- View counts
- Like statistics
- Comment insights
- Subscriber growth

## Testing

```bash
cd backend
python manage.py test
```

## Deployment

### Production Checklist
- [ ] Set DEBUG=False
- [ ] Configure SECRET_KEY
- [ ] Set up PostgreSQL
- [ ] Configure email backend
- [ ] Set up static files
- [ ] Configure CORS properly
- [ ] Use environment variables
- [ ] Set up SSL/HTTPS

### Deployment Options
- Heroku
- AWS
- DigitalOcean
- Azure
- Google Cloud

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues and questions:
- Open an issue on GitHub
- Check documentation
- Contact development team

## Roadmap

- [ ] Real-time notifications with WebSockets
- [ ] Live streaming support
- [ ] Monetization features (ads, subscriptions)
- [ ] AI-powered recommendations
- [ ] Advanced analytics dashboard
- [ ] Mobile app (React Native)
- [ ] Community forums
- [ ] Playlist management
- [ ] Content moderation tools
- [ ] Multi-language support

## Authors

- **Gunraj Kumar** - Initial development

## Acknowledgments

- Django community
- Django REST Framework
- Bootstrap team
- All contributors
