from app.database import classes
from app.models import FitnessClass
from datetime import datetime

def seed_classes():
    classes.clear()
    classes.extend([
        FitnessClass(id=1, name="Yoga", instructor="Aditi", datetime_ist=datetime(2025, 6, 6, 9, 0), available_slots=10),
        FitnessClass(id=2, name="Zumba", instructor="Rahul", datetime_ist=datetime(2025, 6, 6, 11, 0), available_slots=8),
        FitnessClass(id=3, name="HIIT", instructor="John", datetime_ist=datetime(2025, 6, 6, 14, 0), available_slots=5),
    ])