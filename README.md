# 🚀 KPA Backend Assignment - Manthan Kakkar

This project implements two APIs from the provided KPA form data Swagger documentation using Django REST Framework and PostgreSQL.

---

## 🧰 Tech Stack

- Python 3
- Django 4.x
- Django REST Framework
- PostgreSQL
- pgAdmin (for DB management)
- Postman (for testing)
- `.env` configuration using `python-decouple`

---


## 📦 Features Implemented

### 1️⃣ POST `/api/forms/bogie-checksheet/`
- Accepts nested JSON containing:
  - BMBC Checksheet
  - Bogie Checksheet
  - Bogie Details
- Stores them in related models
- Returns full structured response

### 2️⃣ GET `/api/forms/wheel-specifications/`
- Accepts optional filters:
  - `formNumber`
  - `submittedBy`
  - `submittedDate`
- Returns wheel specification entries with nested `fields`
