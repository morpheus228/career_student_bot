from abc import ABC, abstractmethod
import repositories

from repositories.postgres.models import Category, Post, Tag
from services.interfaces import SelectCD
from services.interfaces.mailing import Mailing
from utils.keyboard import make_double_keyboard

from ..interfaces.menu import CategoryСhoiceCD, Menu, TagChoiceCD 

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MailingService(Mailing):
    def __init__(self, preferences_repository: repositories.Preferences, posts_repository: repositories.Posts):
        self.preferences_repository: repositories.Preferences = preferences_repository
        self.posts_repository: repositories.Posts = posts_repository
    
    async def make(self, post: dict):
        post = self.posts_repository.create(text=post['text'], photo=post['photo'], link=post['link'], tags=post['tags'], category=post['category'])
        tags = self.preferences_repository.get_post_tags(post.id)
        category_id = post.category_id

        