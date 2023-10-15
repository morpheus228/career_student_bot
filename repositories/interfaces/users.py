from abc import ABC, abstractmethod
from aiogram import types

from ..postgres.models import User


class Users(ABC):
	@abstractmethod
	def create(self, user: types.User) -> User:
		pass
	
	@abstractmethod
	def get_by_id(self, user_id: int) -> User|None:
		pass

	@abstractmethod
	def update(self, user_id: int, **kwargs):
		pass
	