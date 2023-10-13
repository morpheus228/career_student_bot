from .postgres import *
from .interfaces import *


class Repository:
	def __init__(self, engine):
		self.engine = engine
		
		self.users: Users = UsersPostgres(engine)