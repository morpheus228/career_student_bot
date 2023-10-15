from ..interfaces import Users

from sqlalchemy.orm import Session
from .models import User

from aiogram import types

class UsersPostgres(Users):
    def __init__(self, engine):
        self.engine = engine

    def get_by_id(self, user_id: int) -> User|None:
        with Session(self.engine) as session:
            return session.query(User).get(user_id)
    
    def create(self, user: types.User) -> User:
        with Session(self.engine) as session:

            user = User(id = user.id,
                        username = user.username,
                        first_name = user.first_name,
                        last_name = user.last_name)
        
            session.add(user)
            session.commit()
            
            return user
		
    def update(self, user_id: int, **kwargs):
        user = self.get_by_id(user_id)
            
        with Session(self.engine) as session:
            for attr, value in kwargs.items():
                user.__setattr__(attr, value)

            session.add(user)
            session.commit()
        
        return user
	
    