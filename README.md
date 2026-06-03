<div align="center">

# 📅 Event Management
**A Modern, Role-Based Event Management System**

![Python](https://img.shields.io/badge/PYTHON-3.x+-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/DJANGO-6.0.3-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/POSTGRESQL-PRODUCTION-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Tailwind](https://img.shields.io/badge/TAILWIND_CSS-3.x-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Node](https://img.shields.io/badge/NODE.JS-NPM-339933?style=for-the-badge&logo=node.js&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deploy](https://img.shields.io/badge/Deploy-Render.com-46E3B7?style=flat&logo=render&logoColor=white)](#)

[Live Demo](#) · [Report a Bug](#) · [Request a Feature](#)

</div>

---

## 📖 Table of Contents
- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Project Structure](#-project-structure)
- [License](#-license)

---

## 🌟 About The Project

**EventMaster** is a production-ready, full-stack event management platform built with Django and styled with Tailwind CSS's modern glassmorphism design language. It brings organizers, participants, and administrators together in one unified, role-aware system.

From creating a tech conference to RSVPing for a local music night, EventMaster handles it all — with automated email notifications, advanced search, and a real-time dashboard that gives every user exactly what they need to see.

**💡 Why EventMaster?**
Most event platforms are either too simple or too bloated. EventMaster hits the sweet spot — clean role-based access, a beautiful responsive UI, automated workflows, and a one-command deployment pipeline to Render.com.

---

## ✨ Key Features

* **🎭 Role-Based Access Control:** Distinct dashboards for Admins, Organizers, and Participants.
* **🎨 Premium UI/UX:** Built with Tailwind CSS featuring modern glassmorphism and responsive layouts.
* **🔍 Advanced Search:** Seamlessly search for Artists, Teams, and Venues.
* **📊 Analytics Dashboard:** Real-time statistics for total events, upcoming schedules, and participant counts.
* **✉️ Automated Workflows:** Email notifications and seamless ticket generation.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.14.5 |
| **Framework** | Django 6.0.3 |
| **Database (Local)** | SQLite |
| **Database (Production)** | PostgreSQL |
| **Frontend** | HTML5, Tailwind CSS , FontAwesome |
| **CSS Build Tool** | Node.js + npm |
| **Config Management** | python-decouple |
| **Deployment** | Render.com |

---

## 🚀 Getting Started

### Prerequisites
Ensure the following are installed on your machine:
* [Python >= 3.x](https://www.python.org/downloads/)
* [Node.js & npm](https://nodejs.org/) (Required for Tailwind CSS compilation)
* [Git](https://git-scm.com/)
* *Optional:* PostgreSQL for production-like local setup

### Installation

**Step 1 — Clone the repository**
```bash
git clone https://github.com/ashrafulX/Event_Management
cd Event_Management

python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
npm install
python manage.py makemigrations
python manage.py migrate
python populate_db.py

**# One-time production build**
npm run build:tailwind

**# Or watch for changes during active development**
npm run watch:tailwind
python manage.py runserver



**🎉 Open your browser and go to http://127.0.0.1:8000/**





