<div align="center">

# 📅 Event Management System

**A Django learning project — built while learning Django from scratch**

![Python](https://img.shields.io/badge/Python-3.12.3-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-3.4.19-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## 🎓 About This Project

This is a **learning project** — I built it while learning the basics of Django (models, forms, class-based & function-based views, authentication, and templating). It's not a polished, production-grade app; it's a record of what I learned along the way, so the code quality and structure improve in some places and are messy in others. Feel free to explore, fork it, or point out things I could do better!

The project itself is a simple **Event Management System** where users can create events, categorize them, add participants, and view stats on a dashboard.

---

## ✨ Features

- **Event CRUD** — create, update, delete, and list events with a category, location, date/time, ticket price, and participants (many-to-many)
- **Dashboard** — quick stats for total / upcoming / past events and total participants
- **Upcoming & Past Events** views, plus a **search** feature (search by event name, location, or category)
- **Custom User Model** with profile picture and bio
- **Authentication** — sign up, sign in/out, email-based account activation, password reset, and password change
- **Profile page** — view and edit profile info
- **Tailwind CSS** for styling (with a `create_category`, `create_participant`, and `create_event` form UI)
- **Django Admin** for managing data

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.12.3 |
| **Framework** | Django 6.0.5 |
| **Database** | PostgreSQL |
| **Frontend** | HTML5, Tailwind CSS |
| **CSS Build Tool** | Node.js + npm |
| **Config Management** | python-decouple (`.env` file) |
| **Static Files** | WhiteNoise |
| **Debugging** | django-debug-toolbar |

---

## 📁 Project Structure

```
Event_Management/
├── event_management/   # Project settings, root URLs
├── events/              # Events app — models, views, forms, templates
├── users/               # Custom user model, auth views, profile
├── Core/                # Home page app
├── static/               # Source static files (CSS, images)
├── templates/            # Shared/base templates
├── media/                # User-uploaded files (profile pictures)
├── manage.py
├── populate_db.py       # Script to seed the database with sample data
└── requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [Node.js & npm](https://nodejs.org/) (for Tailwind CSS)
- [PostgreSQL](https://www.postgresql.org/) running locally
- [Git](https://git-scm.com/)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/ashrafulX/Event_Management.git
cd Event_Management
```

**2. Create a virtual environment & activate it**
```bash
python -m venv env

# Windows
env\Scripts\activate

# macOS / Linux
source env/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
npm install
```

**4. Set up environment variables**

Create a `.env` file in the project root (see [Environment Variables](#-environment-variables) below).

**5. Create a PostgreSQL database**
```bash
createdb event_management
```
Or create it manually to match the `NAME`, `USER`, and `PASSWORD` you set in `settings.py` / `.env`.

**6. Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**7. (Optional) Seed some sample data**
```bash
python manage.py shell < populate_db.py
```

**8. Build Tailwind CSS**
```bash
npm run build:tailwind
```

**9. Create a superuser (for the Django admin)**
```bash
python manage.py createsuperuser
```

**10. Run the development server**
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser 🎉

---

## 🔑 Environment Variables

Create a `.env` file in the project root with the following keys:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-app-password
FRONTEND_URL=http://localhost:8000
```

> ⚠️ **Never commit your real `.env` file.** It's already listed in `.gitignore` — keep it that way.

---

## 📚 What I Learned

Building this project helped me practice:
- Django's MVT (Model-View-Template) architecture
- Function-based views vs. class-based views
- Custom user models & Django's authentication system
- ModelForms, form validation, and reusable form mixins
- Many-to-many relationships and `aggregate()` / `Q` queries
- Integrating Tailwind CSS into a Django project
- Managing settings/secrets with environment variables

---

<!-- ## 🗺️ Roadmap / Things to Improve

- [ ] Clean up duplicate/commented-out code (leftover FBV vs CBV experiments)
- [ ] Add proper role-based permissions (Admin / Organizer / Participant)
- [ ] Add automated tests
- [ ] Better error handling and form feedback
- [ ] Reorganize templates and static files more consistently -->

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">

Made while learning Django 🚀

</div>