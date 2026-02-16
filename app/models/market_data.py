from sqlalchemy import Column, Integer, Float, DateTime
from app.database import Base
import datetime

class MarketData(Base):
    __tablename__ = "market_data"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
    volume = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
