from abc import ABC, abstractmethod
from aiogram import types

from ..postgres.models import Post, Tag, Category


class TagsCategories(ABC):
	@abstractmethod
	def get_all_tags(self) -> list[Tag]:
		pass

	@abstractmethod
	def get_all_categories(self) -> list[Category]:
		pass

	@abstractmethod
	def create_tag(self, title: str):
		pass

	@abstractmethod
	def create_category(self, title: str):
		pass

	