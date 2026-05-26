🚀 FastAPI Auth Backend

A production-style FastAPI authentication backend built using FastAPI, PostgreSQL, JWT Authentication, Docker, and SQLAlchemy.

This project demonstrates backend engineering concepts including:

User Authentication
JWT Token Security
Role-Based Access Control (RBAC)
PostgreSQL Integration
Docker Containerization
API Documentation using Swagger/OpenAPI
Clean Backend Architecture
📌 Features

✅ User Registration
✅ Secure Password Hashing using Bcrypt
✅ JWT Authentication
✅ Protected API Routes
✅ Role-Based Access Control (RBAC)
✅ PostgreSQL Database Integration
✅ Dockerized Backend & Database
✅ Swagger/OpenAPI Documentation
✅ Modular FastAPI Project Structure

🛠️ Tech Stack

Category	Technologies
Backend	FastAPI, Python
Database	PostgreSQL
ORM	SQLAlchemy
Authentication	JWT, OAuth2
Security	Passlib (bcrypt)
Containerization	Docker, Docker Compose
Documentation	Swagger/OpenAPI
Version Control	Git & GitHub

📂 Project Structure

fastapi-auth-backend/
│
├── app/
│   ├── auth/
│   │   └── jwt_handler.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── routes/
│   │   └── auth_routes.py
│   │
│   ├── schemas/
│   │   └── user.py
│   │
│   ├── database.py
│   └── main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .gitignore

🔐 Authentication Flow

Register User
→ Hash Password
→ Store User in PostgreSQL

Login User
→ Verify Password
→ Generate JWT Token

Protected Route
→ Verify JWT
→ Validate Role
→ Return Response

🐳 Docker Architecture

FastAPI Container
        ↕
PostgreSQL Container
        ↕
Docker Network

🚀 Getting Started

1️⃣ Clone the Repository
git clone git@github.com:0079567603568sahal/fastapi-auth-backend.git
cd fastapi-auth-backend
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Using Docker Compose
docker-compose up --build

🌐 API Access
Once running:
FastAPI API
http://localhost:8000
Swagger Documentation
http://localhost:8000/docs
ReDoc Documentation
http://localhost:8000/redoc
🔑 Example API Endpoints
Method	Endpoint	Description
POST	/register	Register User
POST	/login	User Login
GET	/profile	Protected User Route
GET	/admin	Admin-only Route

🗄️ Database

This project uses:

PostgreSQL + SQLAlchemy ORM

Features:

Persistent user storage
Role management
Secure authentication data handling
🧠 What I Learned

Through this project, I practised:
Backend API architecture
JWT authentication lifecycle
Secure password hashing
Role-based authorization
Docker container networking
PostgreSQL integration
CI/CD & deployment concepts
Debugging backend systems
🚀 Future Improvements
Refresh Tokens
Email Verification
Password Reset
GitHub Actions CI/CD
Kubernetes Deployment
Cloud Deployment (AWS/Azure/Render)
Monitoring & Logging

🌍 Deployment Goals
This project is being expanded toward:
✅ Cloud Deployment
✅ CI/CD Automation
✅ Production-Style DevOps Workflow
✅ Kubernetes & Container Orchestration

👨‍💻 Author
Muhammed Sahal
Backend & DevOps Engineer
FastAPI • Docker • CI/CD • AWS • Azure • Kubernetes • Python
📍 Kerala, India
GitHub:
https://github.com/0079567603568sahal
⭐ Project Status
Actively Improving & Expanding
Current focus:
Production deployment
GitHub Actions
Cloud infrastructure
Kubernetes integration
