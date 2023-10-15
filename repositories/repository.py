from .postgres import *
from .interfaces import *


class Repository:
	def __init__(self, engine):
		self.engine = engine
		
		self.users: Users = UsersPostgres(engine)
		self.posts: Posts = PostsPostgres(engine)
		self.tags_categories: TagsCategories = TagsCategoriesPostgres(engine)
		self.preferences: Preferences = PreferencesPostgres(engine)
		self.menu: Menu = MenuPostgres(engine)