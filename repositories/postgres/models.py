from sqlalchemy import BigInteger, String, Column, DateTime, ForeignKey, Boolean, Integer, Text, Float, Enum
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(BigInteger, primary_key=True)
    username = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    mailing = Column(Boolean)
    created_at = Column(DateTime(), default=datetime.utcnow)


class Category(Base):
    __tablename__ = 'Categories'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(256))


class Tag(Base):
    __tablename__ = 'Tags'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(256))


class Post(Base):
    __tablename__ = 'Posts'

    id = Column(BigInteger, primary_key=True)

    source_type = Column(Integer)

    text = Column(String(1024))
    photo = Column(String(1024))
    link = Column(String(1024))

    category_id = Column(BigInteger, ForeignKey('Categories.id', ondelete='CASCADE'))

    status = Column(Integer, default=0)
    
    created_at = Column(DateTime(), default=datetime.utcnow)


class PostTag(Base):
    __tablename__ = 'PostTag'

    id = Column(BigInteger, primary_key=True)
    post_id = Column(BigInteger, ForeignKey('Posts.id', ondelete='CASCADE'))
    tag_id = Column(BigInteger, ForeignKey('Tags.id', ondelete='CASCADE'))


class UserTag(Base):
    __tablename__ = 'UserTag'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('Users.id', ondelete='CASCADE'))
    tag_id = Column(BigInteger, ForeignKey('Tags.id', ondelete='CASCADE'))


class UserCategory(Base):
    __tablename__ = 'UserCategory'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('Users.id', ondelete='CASCADE'))
    category_id = Column(BigInteger, ForeignKey('Categories.id', ondelete='CASCADE'))