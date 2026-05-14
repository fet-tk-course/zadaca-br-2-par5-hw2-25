from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator

# TODO: Student A - Definiši svoj SQLModel entitet ovdje
# 

#osnova struktura SQLModel entiteta
class ArrangementBase(SQLModel):
    destination:                    str  
    price:                          float
    duration_days:                  int
    is_active:                      bool
    description:                    Optional[str] = None

    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be a positive number')
        return value

    @field_validator('destination')
    @classmethod
    def destination_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError('Destination must not be empty')
        return value.strip() @field_validator('destination')

    
class Arrangement(ArrangementBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ArrangementCreate(ArrangementBase):
    pass

class ArrangementUpdate(SQLModel):
    destination:                    Optional[str] = None
    price:                          Optional[float] = None
    duration_days:                  Optional[int] = None
    is_active:                      Optional[bool] = None
    description:                    Optional[str] = None