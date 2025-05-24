from pydantic import BaseModel, condecimal, constr, validator
from datetime import datetime

class MovementCreate(BaseModel):
    nameMovement: constr(max_length=100)
    flgTipMovement: constr(min_length=1, max_length=1)
    amountMovement: condecimal(gt=0, max_digits=9, decimal_places=2)
    userMovement: int

    @validator("flgTipMovement")
    def validate_flag(cls, v):
        if v not in ("I", "E"):
            raise ValueError("flgTipMovement debe ser 'I' (ingreso) o 'E' (egreso)")
        return v

class MovementResponse(MovementCreate):
    idMovement: int
    nameMovement: str
    flgTipMovement: str
    amountMovement: float
    userMovement: int
    dateMovement: datetime

    class Config:
        from_attributes = True
