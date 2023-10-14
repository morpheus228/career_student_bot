from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from aiogram import types


from ..interfaces import Posts
from ..postgres.models import Post


class PostsPostgres(Posts):
	def __init__(self, engine):
		self.engine = engine

	def create(self, post: Post) -> int:
		with Session(self.engine) as session:
			session.add(post)
			session.commit()
	
	@abstractmethod
	def get_by_id(self, post_id: int) -> Post|None:
		with Session(self.engine) as session:
			return session.query(Post).get(post_id)
    
	
