from aiogram import BaseMiddleware
from aiogram.types import Update
import repositories


class UserAvailabilityMiddleware(BaseMiddleware):
    def __init__(self, users_repository: repositories.Users):
        self.users_repository: repositories.Users = users_repository

    async def __call__(self, handler, update: Update, data: dict):
        user = update.event.from_user
        
        if not self.users_repository.get_by_id(user.id):
           self.users_repository.create(user)
            
        await handler(update, data)