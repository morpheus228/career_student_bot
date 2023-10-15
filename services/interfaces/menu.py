from abc import ABC, abstractmethod

from aiogram.filters.callback_data import CallbackData


class CategoryСhoiceCD(CallbackData, prefix="choose_category"):
    category_id: int
	

class TagChoiceCD(CallbackData, prefix="select_tag"):
    tag_id: int
    is_selected: bool


class Menu(ABC):
	@abstractmethod
	async def get_categories_keyboard(self):
		pass

	@abstractmethod
	async def get_tags_keyboard(self, category_id: int):
		pass
	
	@abstractmethod	
	async def get_post_ids(self, category_id: int, tag_ids: list[id]):
		pass