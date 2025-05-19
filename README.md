# 🔐 Password Manager API - Thiago Topgian

A secure and modular API for managing passwords, built with **FastAPI**. It supports JWT-based authentication, encryption of sensitive data, and user-secret operations.

---

##  Project Structure

```
app/
├── api/
│   ├── auth_routes.py         # Authentication routes (login, registration)
│   └── secrets_routes.py      # Routes for managing secrets
│
├── core/
│   ├── crypto.py              # Encryption utilities
│   ├── hash_utils.py          # Hashing utilities
│   └── jwt_utils.py           # JWT generation and validation
│
├── models/
│   ├── secret.py              # Secret data model
│   └── user.py                # User data model
│
├── schemas/
│   ├── secret_schema.py       # Pydantic schemas for secrets
│   └── user_schema.py         # Pydantic schemas for users
│
├── database.py                # Database configuration
└── main.py                    # Application entry point

docker/
├── docker-compose.yml         # Docker Compose setup
└── Dockerfile                 # Docker build file

requirements.txt               # Project dependencies
README.md                      # Project documentation
```

---

##  Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [JWT](https://jwt.io/)
- [Docker](https://www.docker.com/)

---

##  Installation

### With Docker

```bash
docker-compose up --build
```

The API will be available at: `http://localhost:8000`

### Manually (without Docker)

```bash
# Clone the repository
git clone https://github.com/your-username/password-manager-api.git
cd password-manager-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```

---

## 🔐 Features

- User registration and login with JWT authentication
- Secure encryption for sensitive data
- CRUD operations for user secrets
- Clean and modular architecture

---

## 📚 API Docs (Swagger)

Available at:

```
http://localhost:8000/docs
```

---

## ✅ TODO

- [ ] Integrate with production-grade database (PostgreSQL, SQLite, etc.)
- [ ] Add automated testing (e.g., pytest)
- [ ] Add rate limiting and brute-force protection
- [ ] Create a frontend web interface

---

## Links that I used:

- https://chatgpt.com/
- https://www.youtube.com/watch?v=DdoncfOdru8
- https://www.youtube.com/watch?v=R26iojTwUv8
- https://stackoverflow.com/questions
- https://www.youtube.com/watch?v=1uFVr15xDGg
- https://git-scm.com/docs

---

