from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional

from database import get_session
from models_a import Arrangement, ArrangementCreate, ArrangementUpdate

router = APIRouter(prefix="/resursi_a", tags=["Resurs A"])

# POST - kreiranje novog aranzmana
@router.post("/", response_model=Arrangement, status_code=status.HTTP_201_CREATED)
def create_arrangement(arrangement: ArrangementCreate, session: Session = Depends(get_session)):
    db_arrangement = Arrangement.model_validate(arrangement)
    session.add(db_arrangement)
    session.commit()
    session.refresh(db_arrangement)
    return db_arrangement

# GET - dohvati sve aranzmane ili filtriraj po destinaciji
@router.get("/", response_model=List[Arrangement])
def read_arrangement(destination: Optional[str] = None, session: Session = Depends(get_session)):
    statement = select(Arrangement)
    if destination:
        statement = statement.where(Arrangement.destination == destination)
    arrangements = session.exec(statement).all()
    return arrangements

# GET by ID- dohvati aranzman po ID-u
@router.get("/{arrangement_id}", response_model=Arrangement)
def read_arrangement_by_id(arrangement_id: int, session: Session = Depends(get_session)):
    arrangement = session.get(Arrangement, arrangement_id)
    if not arrangement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Arrangement not found")
    return arrangement

# PUT - azuriranje cijelog aranzmana
@router.put("/{arrangement_id}", response_model=Arrangement)
def update_arrangement(arrangement_id: int, arrangement: ArrangementCreate, session: Session = Depends(get_session)):
    db_arrangement = session.get(Arrangement, arrangement_id)
    if not db_arrangement:
        raise HTTPException(status_code=404, detail="Arrangement not found")
    
    arrangement_data = arrangement.model_dump()
    for key, value in arrangement_data.items():
        setattr(db_arrangement, key, value)
    
    session.add(db_arrangement)
    session.commit()
    session.refresh(db_arrangement)
    return db_arrangement

# PATCH - djelomicno azuriranje aranzmana
@router.patch("/{arrangement_id}", response_model=Arrangement)
def patch_arrangement(arrangement_id: int, arrangement: ArrangementUpdate, session: Session = Depends(get_session)):
    db_arrangement = session.get(Arrangement, arrangement_id)
    if not db_arrangement:
        raise HTTPException(status_code=404, detail="Arrangement not found")
        
    arrangement_data = arrangement.model_dump(exclude_unset=True)
    for key, value in arrangement_data.items():
        setattr(db_arrangement, key, value)
        
    session.add(db_arrangement)
    session.commit()
    session.refresh(db_arrangement)
    return db_arrangement

# DELETE - brisanje aranzmana
@router.delete("/{arrangement_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_arrangement(arrangement_id: int, session: Session = Depends(get_session)):
    db_arrangement = session.get(Arrangement, arrangement_id)
    if not db_arrangement:
        raise HTTPException(status_code=404, detail="Arrangement not found")

    session.delete(db_arrangement)
    session.commit()
    return None