from abc import ABC, abstractmethod
from aiogram import types

from ..postgres.models import Post


class Posts(ABC):
	@abstractmethod
	def create(self, post: Post) -> int:
		pass
	
	@abstractmethod
	def get_by_id(self, user_id: int) -> Post|None:
		pass
	
