from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, index=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    
    # Game stats
    total_points = Column(Integer, default=0)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    total_taps = Column(Integer, default=0)
    
    # Combo
    current_combo = Column(Integer, default=0)
    max_combo = Column(Integer, default=0)
    last_tap_time = Column(DateTime, nullable=True)
    
    # Daily streak
    daily_streak = Column(Integer, default=0)
    last_daily_claim = Column(DateTime, nullable=True)
    
    # Metadata
    is_bot = Column(Boolean, default=False)
    is_premium = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            "id": self.id,
            "telegram_id": self.telegram_id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "total_points": self.total_points,
            "level": self.level,
            "experience": self.experience,
            "total_taps": self.total_taps,
            "current_combo": self.current_combo,
            "max_combo": self.max_combo,
            "daily_streak": self.daily_streak,
            "is_premium": self.is_premium,
            "created_at": self.created_at.isoformat(),
        }