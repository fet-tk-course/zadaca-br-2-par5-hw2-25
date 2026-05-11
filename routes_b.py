from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional
from database import get_session
from models_b import Booking, BookingCreate, BookingUpdate

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.get("/", response_model=List[Booking])
def read_bookings(
    destination: Optional[str] = None, 
    session: Session = Depends(get_session) 
):
    statement = select(Booking)
    if destination:
        statement = statement.where(Booking.destination == destination)
    
    results = session.exec(statement).all()
    return results

@router.get("/{id}", response_model=Booking)
def read_booking(id: int, session: Session = Depends(get_session)):
    booking = session.get(Booking, id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.post("/", status_code=201)
def create_booking(booking: BookingCreate, session: Session = Depends(get_session)):
    db_booking = Booking.model_validate(booking)
    session.add(db_booking)
    session.commit()
    session.refresh(db_booking)

    return db_booking

@router.put("/{id}", response_model=Booking)
def update_booking_full(id: int, booking: BookingCreate, session: Session = Depends(get_session)):
    db_booking = session.get(Booking, id)
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    booking_data = booking.model_dump()
    for key, value in booking_data.items():
        setattr(db_booking, key, value)
        
    session.add(db_booking)
    session.commit()
    session.refresh(db_booking)
    return db_booking

@router.patch("/{id}", response_model=Booking)
def partial_update_booking(id: int, booking_data: BookingUpdate, session: Session = Depends(get_session)):
    db_booking = session.get(Booking, id)
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    update_data = booking_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_booking, key, value)

    session.commit()
    session.refresh(db_booking)
    return db_booking

@router.delete("/{id}", status_code=204)
def delete_booking(id: int, session: Session = Depends(get_session)):
    booking = session.get(Booking, id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    session.delete(booking)
    session.commit()