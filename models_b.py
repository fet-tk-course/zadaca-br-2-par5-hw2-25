from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from pydantic import field_validator

class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_full_name: str
    customer_email: str
    customer_phone: str
    destination: str
    departure_date: datetime
    return_date: datetime
    number_of_travelers: int
    total_amount: float
    is_paid: bool = Field(default=False)
    payment_method: Optional[str] = None
    status: str = Field(default="pending")
    booking_date: datetime = Field(default_factory=datetime.now)

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

    @field_validator('customer_full_name')
    @classmethod
    def ime_ne_smije_biti_prazno(cls, v):
        if not v.strip():
            raise ValueError('Ime i prezime  ne smije biti prazan string') 
        return v.strip()

    @field_validator('number_of_travelers')
    @classmethod
    def broj_putnika_mora_biti_pozitivan(cls, v):
        if v <= 0:
            raise ValueError('Broj mora biti veći od nule') 
        return v

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