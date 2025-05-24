from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.movement_controller import create_movement, get_movement, update_movement, delete_movement, get_movements
from app.database.connection import get_db
from app.schemas.movement_schema import MovementResponse, MovementCreate
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/api/v1/movements", tags=["Movement"])

@router.get("/", response_model=List[MovementResponse])
def read_movements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_movements = get_movements(db, skip, limit)
    return jsonable_encoder(db_movements)

@router.post("/", response_model=MovementResponse)
def create_movement_endpoint(movement: MovementCreate, db: Session = Depends(get_db)):
    db_obj = create_movement(db, movement)
    return jsonable_encoder(db_obj)

@router.get("/{movement_id}", response_model=MovementResponse)
def read_movement(movement_id: int, db: Session = Depends(get_db)):
    db_movement = get_movement(db, movement_id)
    return jsonable_encoder(db_movement)

@router.put("/{movement_id}", response_model=MovementResponse)
def update_movement_endpoint(movement_id: int, movement: MovementCreate, db: Session = Depends(get_db)):
    db_obj = update_movement(db, movement_id, movement)
    return jsonable_encoder(db_obj)

@router.delete("/{movement_id}")
def delete_movement_endpoint(movement_id: int, db: Session = Depends(get_db)):
    return delete_movement(db, movement_id)
