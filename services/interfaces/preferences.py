from abc import ABC, abstractmethod


class Preferences(ABC):
	@abstractmethod
	async def get_categories_keyboard(self):
		pass

	@abstractmethod
	async def get_tags_keyboard(self):
		pass

	@abstractmethod
	async def set_user_categories(self, user_id: int, categories: list):
		pass

	@abstractmethod
	async def set_user_tags(self, user_id: int, tags: int):
		pass

	@abstractmethod
	async def get_user_categories(self, user_id: int) -> str:
		pass
	
	@abstractmethod
	async def get_user_tags(self, user_id: int) -> str:
		pass
	
	@abstractmethod
	async def get_user_mailing_mode(self, user_id: int) -> bool:
		pass

	@abstractmethod
	async def set_user_mailing_mode(self, user_id: int, mode: bool):
		pass