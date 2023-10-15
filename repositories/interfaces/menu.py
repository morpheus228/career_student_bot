
from abc import ABC, abstractmethod

from repositories.postgres.models import Category, Tag


class Menu(ABC):
	@abstractmethod
	def get_categories(self):
		pass

	@abstractmethod
	def get_tags_by_category(self, tag_id: int):
		pass

	@abstractmethod
	def get_posts(self, category_id: int, tag_ids: list[int]):
		pass
