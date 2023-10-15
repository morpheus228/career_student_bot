from abc import ABC, abstractmethod
import repositories

from repositories.postgres.models import Category, Tag
from utils.keyboard import make_double_keyboard

from ..interfaces import SelectCD
from ..interfaces import Preferences

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


class PreferencesService(Preferences):
	def __init__(self, repository: repositories.TagsCategories, preferences_repository: Preferences, users_repository: repositories.Users):
		self.repository: repositories.TagsCategories = repository
		self.preferences_repository: repositories.Preferences = preferences_repository
		self.user_repository: repositories.Users = users_repository

	async def get_categories_keyboard(self) -> InlineKeyboardMarkup:
		categories = self.repository.get_all_categories()
		categories = [[self.convert_to_button(category, 'category')] for category in categories]
		return InlineKeyboardBuilder(categories).as_markup()

	async def get_tags_keyboard(self) -> InlineKeyboardMarkup:
		tags = self.repository.get_all_tags()
		tags = [self.convert_to_button(tag, 'tag') for tag in tags]
		return InlineKeyboardBuilder(make_double_keyboard(tags)).as_markup()

	async def set_user_categories(self, user_id: int, callback: CallbackQuery):		
		self.preferences_repository.delete_user_categories(user_id)

		inline_keyboard = callback.message.reply_markup.inline_keyboard
        
		for i in range(len(inline_keyboard)):
			for j in range(len(inline_keyboard[i])):
				callback_data = inline_keyboard[i][j].callback_data

				if callback_data != "confirm_categories":
					callback_data = SelectCD.unpack(callback_data)

					if callback_data.is_selected:
						self.preferences_repository.create_user_category(user_id, callback_data.id)

	async def set_user_tags(self, user_id: int, callback: CallbackQuery):
		self.user_repository.update(user_id, mailing=True)
		self.preferences_repository.delete_user_tags(user_id)

		inline_keyboard = callback.message.reply_markup.inline_keyboard
        
		for i in range(len(inline_keyboard)):
			for j in range(len(inline_keyboard[i])):
				callback_data = inline_keyboard[i][j].callback_data

				if callback_data != "confirm_tags":
					callback_data = SelectCD.unpack(callback_data)

					if callback_data.is_selected:
						self.preferences_repository.create_user_tag(user_id, callback_data.id)

	async def get_user_categories(self, user_id: int) -> str:
		categories = self.preferences_repository.get_user_categories(user_id)
		category_titles = [category.title for category in categories]
		return ", ".join(category_titles)
	
	async def get_user_tags(self, user_id: int) -> str:
		tags = self.preferences_repository.get_user_tags(user_id)
		tag_titles = [tag.title for tag in tags]
		return ", ".join(tag_titles)
	
	async def get_user_mailing_mode(self, user_id: int) -> bool:
		user = self.user_repository.get_by_id(user_id)
		return user.mailing
	
	async def set_user_mailing_mode(self, user_id: int, mode: bool):
		self.user_repository.update(user_id, mailing=mode)

	@staticmethod
	def convert_to_button(object, object_type: str):
		return InlineKeyboardButton(
			text=object.title, 
			callback_data=SelectCD(id=object.id, 
						  is_selected=False, 
						  object_type=object_type).pack())