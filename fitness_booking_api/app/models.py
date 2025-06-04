from pydantic import BaseModel, EmailStr
from datetime import datetime

class FitnessClass(BaseModel):
    id: int
    name: str
    instructor: str
    datetime_ist: datetime
    available_slots: int

class Booking(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(Booking):
    booking_time: datetime