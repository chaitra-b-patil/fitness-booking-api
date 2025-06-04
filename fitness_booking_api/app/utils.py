import pytz
from datetime import datetime

def convert_ist_to_timezone(dt: datetime, target_timezone: str) -> datetime:
    ist = pytz.timezone('Asia/Kolkata')
    target = pytz.timezone(target_timezone)
    return ist.localize(dt).astimezone(target)