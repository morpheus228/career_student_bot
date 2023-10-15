from abc import ABC, abstractmethod
import repositories

from repositories.postgres.models import Category, Tag
from services.interfaces import SelectCD
from utils.keyboard import make_double_keyboard

from ..interfaces.menu import CategoryСhoiceCD, Menu, TagChoiceCD 

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MenuService(Menu):
	def __init__(self, repository: repositories.Menu, posts_repository: repositories.Posts):
		self.repository: repositories.Menu = repository
		self.posts_repository: repositories.Posts = posts_repository

	async def get_categories_keyboard(self) -> InlineKeyboardMarkup:
		categories = self.repository.get_categories()
		categories = [self.convert_to_button(category, 'choose_category') for category in categories]
		return InlineKeyboardBuilder([[category] for category in categories]).as_markup()

	async def get_tags_keyboard(self, category_id: int) -> InlineKeyboardMarkup:
		tags = self.repository.get_tags_by_category(category_id)
		tags = [self.convert_to_button(tag, 'choose_tag') for tag in tags]
		return InlineKeyboardBuilder(make_double_keyboard(tags)).as_markup()

	async def get_selected_tags(self, callback: CallbackQuery):
		tags_ids = []

		inline_keyboard = callback.message.reply_markup.inline_keyboard
        
		for i in range(len(inline_keyboard)):
			for j in range(len(inline_keyboard[i])):
				callback_data = inline_keyboard[i][j].callback_data

				if callback_data != "show_posts":
					callback_data = SelectCD.unpack(callback_data)

					if callback_data.is_selected:
						tags_ids.append(callback_data.id)
		
		return tags_ids
	
	async def get_post_ids(self, category_id: int, tag_ids: list[int]):
		return [post[0] for post in self.repository.get_posts(category_id, tag_ids)]
	
	async def get_post_by_id(self, post_id: int):
		return self.posts_repository.get_by_id(post_id)

	@staticmethod
	def convert_to_button(object, object_type: str):
		return InlineKeyboardButton(
			text=object.title, 
			callback_data=SelectCD(id=object.id, 
						  is_selected=False, 
						  object_type=object_type).pack())