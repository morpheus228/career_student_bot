from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from aiogram import types

from .models import Category, Post, PostTag, Tag

from ..interfaces.menu import Menu


class MenuPostgres(Menu):
    def __init__(self, engine):
        self.engine = engine
    
    def get_categories(self):
        with Session(self.engine) as session:
            return session.query(Category).join(Post).all()
    
    def get_tags_by_category(self, category_id: int):
        with Session(self.engine) as session:
            return session.query(Tag).join(PostTag).join(Post).filter(Post.category_id == category_id).all()
    
    def get_posts(self, category_id: int, tag_ids: list[int]):
        with Session(self.engine) as session:
            return session.query(Post.id).filter(Post.category_id == category_id).join(PostTag).filter(PostTag.tag_id.in_(tag_ids)).distinct().all()
    