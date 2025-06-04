# 🧪 Fitness Booking API

A simple FastAPI project for booking fitness classes like Yoga, Zumba, and HIIT.

## 🚀 Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API server:
```bash
uvicorn app.main:app --reload
```

3. Access the docs at:
```
http://127.0.0.1:8000/docs
```

## 📌 Sample Requests

### Get all classes
```bash
curl http://localhost:8000/classes
```

### Book a class
```bash
curl -X POST http://localhost:8000/book \
 -H "Content-Type: application/json" \
 -d '{"class_id":1,"client_name":"John Doe","client_email":"john@example.com"}'
```

### Get bookings by email
```bash
curl "http://localhost:8000/bookings?email=john@example.com"
```

## 📹 Loom Video

👉 Link your Loom walkthrough here.