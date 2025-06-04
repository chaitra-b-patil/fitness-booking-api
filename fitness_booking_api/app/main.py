from fastapi import FastAPI, HTTPException
from app.models import Booking
from app.crud import get_all_classes, book_class, get_bookings_by_email
from app.database import classes  # triggers class storage
from seed_data import seed_classes  # initialize seed data

app = FastAPI()

seed_classes()  # Seed initial classes

@app.get("/classes")
def list_classes():
    return get_all_classes()

@app.post("/book")
def book(data: Booking):
    result = book_class(data)
    if not result:
        raise HTTPException(status_code=400, detail="Class full or invalid ID")
    return result

@app.get("/bookings")
def get_bookings(email: str):
    return get_bookings_by_email(email)