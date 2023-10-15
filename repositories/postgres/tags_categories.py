from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from aiogram import types

from ..interfaces import TagsCategories

from ..interfaces import Posts
from .models import Category, Post, Tag


class TagsCategoriesPostgres(TagsCategories):
	def __init__(self, engine):
		self.engine = engine

	def get_all_tags(self) -> list[Tag]:
		with Session(self.engine) as session:
			return session.query(Tag).all()

	def get_all_categories(self) -> list[Category]:
		with Session(self.engine) as session:
			return session.query(Category).all()
		
	def create_tag(self, title: str):
		with Session(self.engine) as session:
			session.add(Tag(title=title))
			session.commit()

	def create_category(self, title: str):
		with Session(self.engine) as session:
			session.add(Category(title=title))
			session.commit()
	
	def get_category_by_title(self, title: str) -> Category:
		with Session(self.engine) as session:
			return session.query(Category).filter(Category.title == title).first()
		
	def get_tag_by_title(self, title: str) -> Tag:
		with Session(self.engine) as session:
			return session.query(Tag).filter(Tag.title == title).first()
	
    
	
