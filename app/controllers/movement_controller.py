
from sqlalchemy.orm import Session
from app.models.movement_model import Movement
from app.schemas.movement_schema import MovementCreate
from fastapi import HTTPException

def create_movement(db: Session, movement: MovementCreate):
    try:
        db_movement = Movement(**movement.dict())
        db.add(db_movement)
        db.commit()
        db.refresh(db_movement)
        return db_movement
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear el movimiento: {str(e)}")

def get_movements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Movement).offset(skip).limit(limit).all()

def get_movement(db: Session, movement_id: int):
    movement = db.query(Movement).filter(Movement.idMovement == movement_id).first()
    if not movement:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return movement

def update_movement(db: Session, movement_id: int, movement_data: MovementCreate):
    movement = db.query(Movement).filter(Movement.idMovement == movement_id).first()
    if not movement:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    for key, value in movement_data.dict().items():
        setattr(movement, key, value)
    db.commit()
    db.refresh(movement)
    return movement

def delete_movement(db: Session, movement_id: int):
    movement = db.query(Movement).filter(Movement.idMovement == movement_id).first()
    if not movement:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    db.delete(movement)
    db.commit()
    return {"message": "Movimiento eliminado correctamente"}
