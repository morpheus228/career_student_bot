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
	
	def get_by_id(self, post_id: int) -> Post|None:
		with Session(self.engine) as session:
			return session.query(Post).get(post_id)
		
	def get_all(self) -> list[Post]:
		with Session(self.engine) as session:
			return session.query(Post).all()

	def update(self, post_id: int, **kwargs):
		post = self.get_by_id(post_id)

		with Session(self.engine) as session:
			for attr, value in kwargs:
				post.__setattr__(attr, value)
			session.commit()
		
		return post
	
    
	
