from sqlalchemy.orm import Session

from ..interfaces import Preferences
from .models import Category, PostTag, Tag, UserCategory, UserTag


class PreferencesPostgres(Preferences):
	def __init__(self, engine):
		self.engine = engine

	def create_user_tag(self, user_id: int, tag_id: int):
		with Session(self.engine) as session:
			session.add(UserTag(user_id=user_id, tag_id=tag_id))
			session.commit()

	def create_user_category(self, user_id: int, category_id: int):
		with Session(self.engine) as session:
			session.add(UserCategory(user_id=user_id, category_id=category_id))
			session.commit()

	def delete_user_tags(self, user_id: int):
		with Session(self.engine) as session:
			session.query(UserTag).filter(UserTag.user_id == user_id).delete()
			session.commit()

	def delete_user_categories(self, user_id: int):
		with Session(self.engine) as session:
			session.query(UserCategory).filter(UserCategory.user_id == user_id).delete()
			session.commit()

	def get_user_categories(self, user_id: int) -> list[Category]:
		with Session(self.engine) as session:
			user_categories = session.query(UserCategory).filter(UserCategory.user_id == user_id).all()
			return [session.query(Category).get(category.category_id) for category in user_categories]
    
	def get_user_tags(self, user_id: int) -> list[Tag]:
		with Session(self.engine) as session:
			user_tags = session.query(UserTag).filter(UserTag.user_id == user_id).all()
			return [session.query(Tag).get(tag.tag_id) for tag in user_tags]
		
	def get_post_tags(self, post_id: int) -> list[Tag]:
		with Session(self.engine) as session:
			post_tags = session.query(PostTag).filter(PostTag.post_id == post_id).all()
			return [session.query(Tag).get(tag.tag_id) for tag in post_tags]
