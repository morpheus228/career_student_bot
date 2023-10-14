from aiogram import Bot
from config import Config
from repositories import Repository

from .realizations import *
from .interfaces import *


class Service:
	def __init__(self, repository: Repository, config: Config, bot: Bot):
		self.forms: Forms = FormsService(repository.forms, bot)
		self.swiping: Swiping = SwipingService(repository.swiping, repository.rates, repository.matches, self.forms)
		self.answers: Answers = AnswersService()

