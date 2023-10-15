from aiogram import Bot
from config import Config
from repositories import Repository

from .realizations import *
from .interfaces import *


class Service:
	def __init__(self, repository: Repository):
		self.preferences: Preferences = PreferencesService(repository.tags_categories, repository.preferences, repository.users)
		self.menu: Menu = MenuService(repository.menu, repository.posts)
		self.mailing: Mailing = MailingService(repository.menu, repository.posts)

