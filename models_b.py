from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Podaci o klijentu
    customer_full_name: str
    customer_email: str
    customer_phone: str

    # Podaci o putovanju
    destination: str
    departure_date: datetime
    return_date: datetime
    number_of_travelers: int

    # Podaci o plaćanju
    total_amount: float
    is_paid: bool = Field(default=False)
    payment_method: Optional[str] = None

    status: str = Field(default="pending")
    booking_date: datetime = Field(default_factory=datetime.now)

# 2. Shema za kreiranje (XCreate)
class BookingCreate(SQLModel):
    customer_full_name: str
    customer_email: str
    customer_phone: str
    destination: str
    departure_date: datetime
    return_date: datetime
    number_of_travelers: int
    total_amount: float
    is_paid: bool = False
    payment_method: Optional[str] = None
    status: str = "pending"

# 3. Shema za ažuriranje (XUpdate)
class BookingUpdate(SQLModel):
    customer_full_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None
    destination: Optional[str] = None
    departure_date: Optional[datetime] = None
    return_date: Optional[datetime] = None
    number_of_travelers: Optional[int] = None
    total_amount: Optional[float] = None
    is_paid: Optional[bool] = None
    payment_method: Optional[str] = None
    status: Optional[str] = None