🍋 Little Lemon Booking API

This is a Django REST Framework project that provides APIs for managing restaurant bookings and menu items for Little Lemon restaurant.

🚀 Features

✅ User registration and authentication using JWT (Djoser)

✅ Booking API (create, list, update, delete bookings)

✅ Menu Items API (CRUD operations)

✅ Permissions and role-based access

✅ Unit testing with TestCase

✅ Connected to MySQL / SQLite database

✅ Deployed to GitHub


🛠️ Tech Stack

Python 3.11+

Django 4.x

Django REST Framework

Djoser (JWT Auth)

SQLite / MySQL

Git & GitHub



📦 Installation

git clone https://github.com/BaderAlt/lemon-booking-project.git

cd lemon-booking-project

pip install -r requirements.txt

python manage.py migrate




▶️ Run the Server

python manage.py runserver




Then open:

http://127.0.0.1:8000/





🔐 Authentication

Use Djoser endpoints for auth:

POST /auth/users/ – Register

POST /auth/jwt/create/ – Login (get JWT)

POST /auth/jwt/verify/ – Verify token

POST /auth/jwt/refresh/ – Refresh token





🧪 Running Tests

python manage.py test


📝 License
MIT License © 2025 Bader Alt
