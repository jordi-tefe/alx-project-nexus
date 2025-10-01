# 🗳️ ALX Project Nexus – Online Poll System

A backend application built with **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**, designed for managing polls, user authentication, and voting.  

This project was developed as part of the **ALX Project Nexus backend learning journey**.
**Hosted -> https://alx-project-nexus-1-ym5a.onrender.com/**

---

## 🚀 Features

### 🔐 Authentication & Authorization
- JWT-based login & token refresh (via SimpleJWT)  
- User registration & logout  

### ⚙️ Admin Panel
- Access Django’s powerful `/admin/` panel  
- **Superuser created automatically** (see credentials below)  

### 📊 Poll Management (CRUD)
- Create, read, update, delete polls  
- Manage via API endpoints  

### 🗳️ Voting System
- Cast votes on polls  
- Prevent duplicate voting per user  

### 📖 API Documentation
- Swagger UI available at: **`/api/docs/`**

---

## 🛠️ Tech Stack
- **Backend Framework:** Django 5 + Django REST Framework  
- **Database:** PostgreSQL (Render-hosted)  
- **Authentication:** JWT (djangorestframework-simplejwt)  
- **Docs:** Swagger (drf-yasg)  
- **Deployment:** Render (Free Tier)  

---

## 📦 Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/jordi-tefe/alx-project-nexus.git
cd alx-project-nexus/online_poll_backend

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Setup .env file

Create a .env file inside online_poll_backend/ with:

SECRET_KEY=iamjordii
DEBUG=True
DATABASE_URL=postgres://<username>:<password>@<host>:5432/<dbname>

5. Run migrations
python manage.py migrate

6. Create superuser (if needed)
python manage.py createsuperuser


(By default, one admin user is auto-created — see credentials below)

7. Start development server
python manage.py runserver


Now visit 👉 http://127.0.0.1:8000/

🔑 Default Admin Credentials

Username: admin

Password: jordi1993

Email: jordisavage90@gmail.com

Access at 👉 /admin/

📡 API Endpoints
Route	Method	Description
/	GET	Welcome page with available routes
/admin/	GET	Django Admin Panel
/api/auth/register/	POST	Register a new user
/api/auth/login/	POST	Obtain JWT access & refresh tokens
/api/auth/refresh/	POST	Refresh JWT token
/api/auth/logout/	POST	Logout user (blacklist token)
/api/polls/	CRUD	Poll management (create/read/update/delete)
/api/vote/	POST	Cast a vote
/api/docs/	GET	Swagger API documentation
🌍 Deployment (Render)

Backend: Render Web Service

Database: Render PostgreSQL (free instance)

🧑‍💻 Author

Yordanos Teferi

GitHub: @jordi-tefe

Email: jordisavage90@gmail.com
