from abc import ABC, abstractmethod
from aiogram import types

from ..postgres.models import Post


class Posts(ABC):
	@abstractmethod
	def get_all(self) -> list[Post]:
		pass

	@abstractmethod
	def create(self, text: str, photo: str, link: str, category: str, tags: list[str], source_type: int = 0) -> Post:
		pass

	@abstractmethod
	def create_tag(self, post_id: int):
		pass
	
	@abstractmethod
	def get_by_id(self, user_id: int) -> Post|None:
		pass

	@abstractmethod
	def update(self, post_id: int, **kwargs):
		pass
	
