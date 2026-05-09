from sqlmodel import SQLModel, Field
from typing import Optional

# TODO: Student A - Definiši svoj SQLModel entitet ovdje
# 

//osnova struktura SQLModel entiteta
class ArrangementBase(SQLModel):
    destination:                    str     
    price:                          float
    duration_days:                  int
    is_active:                      bool
    description:                    Optional[str] = None

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