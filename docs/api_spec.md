
# 🧾 OwlyWise API Specification

> Version: 1.0  
> Base URL: `/api/v1`  
> Authentication: Bearer Token (JWT)

---

## 📌 Overview

The OwlyWise API powers the personal budgeting app, supporting user accounts, budget tracking, transaction management, and insights. All requests and responses are in `application/json`.

---

## 🔐 Authentication

### POST `/auth/register`

**Registers a new user.**

#### Request Body
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "password": "securePassword123"
}
```

#### Response
```json
{
  "message": "User registered successfully."
}
```

---

### POST `/auth/login`

**Logs in and returns a JWT.**

#### Request Body
```json
{
  "email": "jane@example.com",
  "password": "securePassword123"
}
```

#### Response
```json
{
  "access_token": "<JWT_TOKEN>"
}
```

---

## 👤 User

### GET `/user/profile`

**Returns user profile details.**

> 🔒 Requires Authorization header with `Bearer <token>`

#### Response
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "created_at": "2025-06-01"
}
```

---

## 💸 Budget

### POST `/budget/create`

**Create a new monthly budget.**

#### Request Body
```json
{
  "month": "2025-07",
  "income": 5000,
  "categories": {
    "Rent": 1500,
    "Groceries": 600,
    "Entertainment": 300
  }
}
```

#### Response
```json
{
  "message": "Budget created."
}
```

---

### GET `/budget/current`

**Returns the active monthly budget.**

#### Response
```json
{
  "month": "2025-07",
  "income": 5000,
  "categories": {
    "Rent": 1500,
    "Groceries": 600,
    "Entertainment": 300
  },
  "total_spent": 3200,
  "remaining": 1800
}
```

---

## 💳 Transactions

### POST `/transactions/add`

**Adds a transaction.**

#### Request Body
```json
{
  "amount": 45.50,
  "category": "Groceries",
  "description": "Whole Foods",
  "date": "2025-07-03"
}
```

#### Response
```json
{
  "message": "Transaction added."
}
```

---

### GET `/transactions`

**Returns all transactions for the current month.**

#### Response
```json
[
  {
    "id": 1,
    "amount": 45.50,
    "category": "Groceries",
    "description": "Whole Foods",
    "date": "2025-07-03"
  },
  {
    "id": 2,
    "amount": 1200.00,
    "category": "Rent",
    "description": "July Rent",
    "date": "2025-07-01"
  }
]
```

---

## 📊 Insights (Machine Learning Future)

### GET `/insights/predict-expenses`

**[Future] Predict upcoming expenses based on history.**

#### Response (example)
```json
{
  "predicted_total": 3100,
  "category_predictions": {
    "Groceries": 650,
    "Entertainment": 400,
    "Transport": 150
  }
}
```

---

## 🧪 Health Check

### GET `/health`

**Returns server status.**

#### Response
```json
{
  "status": "ok",
  "uptime": "48h"
}
```

---

## 🔚 Notes

- All dates are formatted as `YYYY-MM-DD`.
- All monetary values are in USD (float).
- API errors return JSON with `error` and `message` fields.

---
