
from abc import ABC, abstractmethod

from repositories.postgres.models import Category, Tag


class Preferences(ABC):
	@abstractmethod
	def create_user_tag(self, user_id: int, tag_id: int):
		pass

	@abstractmethod
	def create_user_category(self, user_id: int, category_id: int):
		pass

	@abstractmethod
	def delete_user_tags(self, user_id: int):
		pass

	@abstractmethod
	def delete_user_categories(self, user_id: int):
		pass

	@abstractmethod
	def get_user_categories(self, user_id: int) -> list[Category]:
		pass

	@abstractmethod
	def get_user_tags(self, user_id: int) -> list[Tag]:
		pass

	@abstractmethod
	def get_post_tags(self, post_id: int) -> list[Tag]:
		pass