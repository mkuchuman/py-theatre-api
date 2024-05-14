# Py-Theatre API

## 🎬 Introduction
**Py-Theatre API** provides a robust platform for managing cinema functionalities such as ticket bookings, performance, and user authentication. This guide details how to set up and run the API locally.

## 🌟 Features

- **JWT Authentication**: Secure access with JSON Web Tokens.
- **Admin Panel**: Comprehensive backend management.
- **Swagger Documentation**: Accessible at `/api/doc/swagger/`.
- **Reservations Management**: Efficient handling of reservations and tickets.
- **Play Management**: Create and modify play details including genres and actors.
- **Theatre Halls**: Manage theatre halls configurations.
- **Performance Scheduling**: Manage performance.

## 🛠 Prerequisites

- **Docker** (for Docker setup)
- **Python 3.8** or higher
- **PostgreSQL**
- **Git**

## ⚙️ Installation

### 🐳 Option 1: Running with Docker

Ensure **Docker** is installed on your system, then follow these steps:

```bash
git clone https://github.com/mkuchuman/py-theatre-api.git
cd py-theatre-api
docker-compose build
docker-compose up
```


### 🖥 Option 2: Installing using GitHub

Clone the repository and set up the environment:

```bash
git clone https://github.com/mkuchuman/py-theatre-api.git
cd py-theatre-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure your database connection
export DB_HOST=<your db hostname>
export DB_NAME=<your db name>
export DB_USER=<your db username>
export DB_PASSWORD=<your db user password>
export SECRET_KEY=<your secret key>

# Apply migrations and run the server
python manage.py migrate
python manage.py runserver
