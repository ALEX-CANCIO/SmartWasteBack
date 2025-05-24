

from sqlalchemy import Column, Integer, String, Numeric, DateTime

from app.database.connection import Base
from datetime import datetime

class Movement(Base):
    __tablename__ = "movements"

    idMovement = Column(Integer, primary_key=True, autoincrement=True)
    nameMovement = Column(String(100), nullable=False)
    flgTipMovement = Column(String(1), nullable=False)
    amountMovement = Column(Numeric(9, 2), nullable=False)
    userMovement = Column(Integer, nullable=False)
    dateMovement = Column(DateTime, default=datetime.utcnow)