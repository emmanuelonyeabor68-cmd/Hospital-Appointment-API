# 🏥 Hospital Appointment API

A backend API built with Django Rest Framework for managing hospital appointments with role-based access control.

---

## 🚀 Features

* User Registration & Authentication (JWT)
* Role-based access (Patient & Doctor)
* Patients can:

  * Create appointments
  * View their appointments
  * Cancel appointments
* Doctors can:

  * View assigned appointments
    
* Secure API endpoints with permissions
* Clean and scalable structure

---

## 🧠 Roles & Permissions

### 👤 Patient

* Can create appointments
* Can view only their appointments
* Can cancel their appointments

### 🩺 Doctor

* Cannot create appointments
* Can view appointments assigned to them

---

## 🛠️ Tech Stack

* Python
* Django
* Django Rest Framework
* JWT Authentication (SimpleJWT)

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/hospital-appointment-api.git
cd hospital-appointment-api
```

### Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

---

## 🧱 Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ▶️ Run Server

```bash
python manage.py runserver
```

---

## 🔑 Authentication

Get token:

```http
POST /api/token/
```

Use in headers:

```
Authorization: Bearer <your_token>
```

---

## 📌 API Endpoints

### 🔹 Auth

* `POST /api/register/`
* `POST /api/token/`

### 🔹 Appointments

* `GET /appointments/`
* `POST /appointments/`
* `DELETE /appointments/{id}/cancel/`

---

## 🧪 Example Request

### Create Appointment (Patient only)

```json
{
  "doctor_user": 2,
  "date": "2026-06-29",
  "time": "10:00"
}
```

---

## 📁 Project Structure

```
hospital-project/
│
├── manage.py
├── .gitignore
├── requirements.txt
│
├── users/
├── appointments/
└── config/
```

---

## 📌 Notes

* Role-based permission is enforced at the view level
* Only patients are allowed to create appointments
* Doctors are restricted from performing certain actions

---

## 🚀 Future Improvements

* Appointment validation (time conflicts)
* Doctor availability scheduling
* Pagination & filtering
* Production deployment setup

---

Built as part of my backend development journey, focusing on building real-world APIs and understanding system design step by step.
