from sqlalchemy import Column, Integer, Float, String, DateTime
from app.database import Base
import datetime

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String)
    entry = Column(Float)
    exit = Column(Float)
    risk = Column(Float)
    reward = Column(Float)
    result_r = Column(Float)
    session = Column(String)
    impulsive = Column(Integer)  # 1 yes, 0 no
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
