from .database import classes, bookings
from .models import Booking, BookingOut
from datetime import datetime

def get_all_classes():
    return classes

def book_class(data: Booking):
    for cls in classes:
        if cls.id == data.class_id:
            if cls.available_slots <= 0:
                return None
            cls.available_slots -= 1
            booking = BookingOut(**data.dict(), booking_time=datetime.now())
            bookings.append(booking)
            return booking
    return None

def get_bookings_by_email(email: str):
    return [b for b in bookings if b.client_email == email]