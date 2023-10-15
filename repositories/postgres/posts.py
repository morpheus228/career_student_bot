from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from aiogram import types


from ..interfaces import Posts
from ..postgres.models import Category, Post, PostTag, Tag


class PostsPostgres(Posts):
	def __init__(self, engine):
		self.engine = engine

	def create(self, text: str, link: str, category: str, tags: list[str], photo: str = None, source_type: int = 0) -> int:
		with Session(self.engine) as session:
			category = session.query(Category).filter(Category.title == category).first()
			post = Post(text=text, photo=photo, link=link, source_type=source_type, category_id=category.id)
			session.add(post)
			session.commit()
		
			for tag_title in tags:
				tag = session.query(Tag).filter(Tag.title == tag_title).first()
				if tag is None:
					tag = Tag(title=tag_title)
					session.add(tag)
					session.commit()
					
				session.add(PostTag(post_id=post.id, tag_id=tag.id))

			session.commit()
			
		return post
	
	def get_by_id(self, post_id: int) -> Post|None:
		with Session(self.engine) as session:
			return session.query(Post).get(post_id)
		
	def get_all(self) -> list[Post]:
		with Session(self.engine) as session:
			return session.query(Post).all()

	def update(self, post_id: int, **kwargs):
		post = self.get_by_id(post_id)

		with Session(self.engine) as session:
			for attr, value in kwargs.items():
				post.__setattr__(attr, value)
			
			session.add(post)
			session.commit()
		
		return post
	
	def create_tag(self, post_id: int, tag_id: int):
		with Session(self.engine) as session:
			session.add(PostTag(post_id=post_id, tag_id=tag_id))
			session.commit()
    
	
