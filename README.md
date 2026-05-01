# FastAPI Blog API 🚀

A RESTful Blog API built with **FastAPI**, featuring JWT authentication, CRUD operations, and user management.

## 🌐 Live Demo

**API URL:** [https://fastapi-learning-k0ev.onrender.com](https://fastapi-learning-k0ev.onrender.com)

**Swagger Docs:** [https://fastapi-learning-k0ev.onrender.com/docs](https://fastapi-learning-k0ev.onrender.com/docs)

## ✨ Features

- **JWT Authentication** — Secure login with OAuth2 + Bearer tokens
- **Blog CRUD** — Create, Read, Update, Delete blog posts
- **User Management** — User registration and profile viewing
- **Interactive API Docs** — Auto-generated Swagger UI

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM / Database |
| [SQLite](https://www.sqlite.org/) | Database |
| [python-jose](https://github.com/mpdavis/python-jose) | JWT tokens |
| [Passlib](https://passlib.readthedocs.io/) + bcrypt | Password hashing |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |
| [Render](https://render.com/) | Deployment |

## 📁 Project Structure

```
FastAPI/
├── blog/
│   ├── main.py              # App entry point
│   ├── models.py             # SQLAlchemy models
│   ├── schemas.py            # Pydantic schemas
│   ├── database.py           # Database configuration
│   ├── hashing.py            # Password hashing
│   ├── token.py              # JWT token creation & verification
│   ├── oauth2.py             # OAuth2 authentication
│   ├── routers/
│   │   ├── authentication.py # Login endpoint
│   │   ├── blog.py           # Blog CRUD endpoints
│   │   └── user.py           # User endpoints
│   └── repository/
│       ├── blog.py           # Blog database operations
│       └── user.py           # User database operations
├── requirements.txt
└── README.md
```

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|---|---|---|
| POST | `/login` | Login and get JWT token |

### Blogs
| Method | Endpoint | Description |
|---|---|---|
| GET | `/blog/` | Get all blogs |
| POST | `/blog/` | Create a new blog |
| GET | `/blog/{id}` | Get a specific blog |
| PUT | `/blog/{id}` | Update a blog |
| DELETE | `/blog/{id}` | Delete a blog |

### Users
| Method | Endpoint | Description |
|---|---|---|
| POST | `/user/` | Register a new user |
| GET | `/user/{id}` | Get user profile |

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/ksskarthik18/FastAPI_learning.git
cd FastAPI_learning

# Create virtual environment
python -m venv blog-env
blog-env\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo SECRET_KEY=your-secret-key-here > .env
echo ALGORITHM=HS256 >> .env
echo ACCESS_TOKEN_EXPIRES_MINUTES=30 >> .env

# Run the server
uvicorn blog.main:app --reload
```

Then open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to see the Swagger UI.

## 📝 License

This project is for learning purposes, following the [Bitfumes FastAPI Tutorial](https://www.youtube.com/c/Bitfumes).
