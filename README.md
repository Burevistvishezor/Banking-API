# Banking API 🏦

A production-ready banking system backend built with FastAPI. This project demonstrates modern Python web development practices with JWT authentication, PostgreSQL, and SQLAlchemy ORM.

![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?logo=postgresql)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Database Schema](#database-schema)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Documentation](#api-documentation)
- [Usage Examples](#usage-examples)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### User Management
- ✅ User registration with email validation
- ✅ Secure login with JWT token generation
- ✅ Password hashing with bcrypt
- ✅ User profile management
- ✅ Token refresh mechanism

### Account Management
- ✅ Create multiple bank accounts per user
- ✅ View account balance in real-time
- ✅ List all accounts for a user
- ✅ Account type management (Checking, Savings, etc.)

### Transactions
- ✅ Money transfer between accounts
- ✅ Deposit and withdrawal operations
- ✅ Complete transaction history with timestamps
- ✅ Transaction status tracking

### Security
- ✅ JWT-based authentication
- ✅ Role-based access control (RBAC)
- ✅ Password encryption
- ✅ Request validation with Pydantic
- ✅ CORS protection

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **FastAPI** | Modern, fast web framework for building APIs |
| **Python 3.11+** | Core programming language |
| **PostgreSQL** | Reliable relational database |
| **SQLAlchemy** | SQL toolkit and ORM for Python |
| **Pydantic** | Data validation and serialization |
| **JWT (PyJWT)** | Token-based authentication |
| **bcrypt** | Password hashing and verification |
| **Docker** | Containerization and deployment |
| **Uvicorn** | ASGI web server |

## 🏗 Project Architecture

```
banking_api/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration management
│   │   └── security.py        # JWT and password utilities
│   │
│   ├── database.py            # Database connection & session
│   │
│   ├── models/                # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── account.py
│   │   └── transaction.py
│   │
│   ├── schemas/               # Pydantic request/response models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── account.py
│   │   └── transaction.py
│   │
│   ├── routers/               # API route handlers
│   │   ├── __init__.py
│   │   ├── auth.py           # Authentication endpoints
│   │   ├── users.py          # User management endpoints
│   │   ├── accounts.py       # Account management endpoints
│   │   └── transactions.py   # Transaction endpoints
│   │
│   └── services/              # Business logic layer
│       ├── __init__.py
│       ├── account_service.py
│       └── transaction_service.py
│
├── migrations/                # Alembic database migrations (optional)
├── tests/                     # Test suite
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_accounts.py
│   └── test_transactions.py
│
├── .env.example              # Environment variables template
├── .gitignore               # Git ignore patterns
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Project configuration
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker services orchestration
└── README.md              # This file
```

## 🗄 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Accounts Table
```sql
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    account_type VARCHAR(50),
    balance DECIMAL(15, 2) DEFAULT 0.00,
    currency VARCHAR(3) DEFAULT 'USD',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Transactions Table
```sql
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    from_account_id INTEGER REFERENCES accounts(id) ON DELETE SET NULL,
    to_account_id INTEGER REFERENCES accounts(id) ON DELETE SET NULL,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_type VARCHAR(50),
    status VARCHAR(50) DEFAULT 'completed',
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 📦 Installation

### Prerequisites
- Python 3.11 or higher
- PostgreSQL 15 or higher
- Docker & Docker Compose (optional)
- pip or poetry

### Setup Instructions

#### 1. Clone the Repository
```bash
git clone https://github.com/Burevistvishezor/Banking-API.git
cd Banking-API
```

#### 2. Create Virtual Environment
```bash
# Using venv
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your settings
nano .env
```

Example `.env` file:
```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/banking_api

# JWT
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Server
DEBUG=True
SERVER_NAME=localhost
SERVER_PORT=8000
```

#### 5. Initialize the Database
```bash
# Run migrations (if using Alembic)
alembic upgrade head

# Or create tables manually
python -m app.database
```

#### 6. Run the Server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## 🚀 Quick Start with Docker

The easiest way to get started:

```bash
# Clone the repository
git clone https://github.com/Burevistvishezor/Banking-API.git
cd Banking-API

# Copy environment file
cp .env.example .env

# Start the services
docker-compose up -d

# View logs
docker-compose logs -f api
```

The API will be available at `http://localhost:8000`

To stop the services:
```bash
docker-compose down
```

## 📚 API Documentation

### Interactive Documentation
Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Authentication Endpoints

#### Register User
```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "john_doe",
  "password": "secure_password_123",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "john_doe",
  "first_name": "John",
  "last_name": "Doe",
  "is_active": true,
  "created_at": "2024-01-15T10:30:00Z"
}
```

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secure_password_123"
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "username": "john_doe"
  }
}
```

### Account Endpoints

#### Create Account
```http
POST /accounts
Authorization: Bearer {token}
Content-Type: application/json

{
  "account_type": "Checking",
  "currency": "USD"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "user_id": 1,
  "account_number": "ACC-1704076200-001",
  "account_type": "Checking",
  "balance": 0.00,
  "currency": "USD",
  "is_active": true,
  "created_at": "2024-01-15T10:30:00Z"
}
```

#### Get All User Accounts
```http
GET /accounts
Authorization: Bearer {token}
```

**Response (200 OK):**
```json
{
  "accounts": [
    {
      "id": 1,
      "user_id": 1,
      "account_number": "ACC-1704076200-001",
      "account_type": "Checking",
      "balance": 5000.00,
      "currency": "USD",
      "is_active": true
    }
  ],
  "total": 1
}
```

#### Get Account by ID
```http
GET /accounts/{account_id}
Authorization: Bearer {token}
```

### Transaction Endpoints

#### Transfer Money
```http
POST /transactions/transfer
Authorization: Bearer {token}
Content-Type: application/json

{
  "from_account_id": 1,
  "to_account_id": 2,
  "amount": 100.00,
  "description": "Payment for services"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "from_account_id": 1,
  "to_account_id": 2,
  "amount": 100.00,
  "transaction_type": "transfer",
  "status": "completed",
  "description": "Payment for services",
  "created_at": "2024-01-15T10:35:00Z"
}
```

#### Get Transaction History
```http
GET /transactions
Authorization: Bearer {token}
```

**Response (200 OK):**
```json
{
  "transactions": [
    {
      "id": 1,
      "from_account_id": 1,
      "to_account_id": 2,
      "amount": 100.00,
      "transaction_type": "transfer",
      "status": "completed",
      "description": "Payment for services",
      "created_at": "2024-01-15T10:35:00Z"
    }
  ],
  "total": 1
}
```

## 💡 Usage Examples

### Python Example using `requests`
```python
import requests

BASE_URL = "http://localhost:8000"

# Register
response = requests.post(f"{BASE_URL}/auth/register", json={
    "email": "user@example.com",
    "username": "john_doe",
    "password": "secure_password",
    "first_name": "John",
    "last_name": "Doe"
})
print(response.json())

# Login
response = requests.post(f"{BASE_URL}/auth/login", json={
    "email": "user@example.com",
    "password": "secure_password"
})
token = response.json()["access_token"]

# Create Account
headers = {"Authorization": f"Bearer {token}"}
response = requests.post(f"{BASE_URL}/accounts", headers=headers, json={
    "account_type": "Checking",
    "currency": "USD"
})
account = response.json()
print(f"Created account: {account['account_number']}")

# Transfer Money
response = requests.post(f"{BASE_URL}/transactions/transfer", headers=headers, json={
    "from_account_id": 1,
    "to_account_id": 2,
    "amount": 100.00,
    "description": "Payment"
})
print(response.json())
```

### cURL Example
```bash
# Register
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "john_doe",
    "password": "secure_password",
    "first_name": "John",
    "last_name": "Doe"
  }'

# Login
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "secure_password"
  }'

# Create Account (replace TOKEN with actual token)
curl -X POST http://localhost:8000/accounts \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "account_type": "Checking",
    "currency": "USD"
  }'
```

## 🔧 Development

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_auth.py -v
```

### Code Quality
```bash
# Format code with black
black app/

# Lint with pylint
pylint app/

# Type checking with mypy
mypy app/
```

### Pre-commit Hooks
```bash
# Install pre-commit
pip install pre-commit

# Install the git hook scripts
pre-commit install

# Run against all files
pre-commit run --all-files
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Banking-API.git
   cd Banking-API
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes and commit**
   ```bash
   git commit -m 'Add amazing feature'
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

5. **Open a Pull Request**

### Coding Standards
- Follow PEP 8 style guide
- Add type hints to functions
- Write docstrings for classes and functions
- Add tests for new features
- Update documentation

### Commit Message Format
```
[TYPE] Brief description

Detailed explanation (optional)

Fixes #ISSUE_NUMBER (if applicable)
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Burevistvishezor**
- GitHub: [@Burevistvishezor](https://github.com/Burevistvishezor)
- Email: Contact via GitHub

## 🔗 Related Projects

- [REST-API-JWT](https://github.com/Burevistvishezor/REST-API-JWT) - Flask JWT authentication example
- [C-Backend-Developer](https://github.com/Burevistvishezor/C-Backend-Developer) - C++ backend development portfolio

## 📞 Support

If you encounter any issues or have questions:
1. Check the [GitHub Issues](https://github.com/Burevistvishezor/Banking-API/issues)
2. Review the [API Documentation](http://localhost:8000/docs)
3. Create a new issue with detailed information

## 🙏 Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- Banking system best practices from industry standards

---

**Made with ❤️ by Burevistvishezor**

⭐ If you find this project helpful, please give it a star!
