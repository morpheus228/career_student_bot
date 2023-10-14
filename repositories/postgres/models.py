from sqlalchemy import BigInteger, String, Column, DateTime, ForeignKey, Boolean, Integer, Text, Float, Enum
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(BigInteger, primary_key=True)
    username = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    created_at = Column(DateTime(), default=datetime.utcnow)


class Post(Base):
    __tablename__ = 'Users'

    id = Column(BigInteger, primary_key=True)
    source_type = Column(Integer)

    text = Column(String(100))
    photo = Column(String(256))
    link = Column(String(1024))

    status = Column(String(100))
    
    created_at = Column(DateTime(), default=datetime.utcnow)

