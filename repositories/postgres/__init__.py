from sqlalchemy import create_engine

from config import PostgresConfig

from .users import UsersPostgres
from .posts import PostsPostgres
from .tags_categories import TagsCategoriesPostgres
from .preferences import PreferencesPostgres
from .menu import MenuPostgres

from .models import Base


def get_engine(config: PostgresConfig):
	engine_str = f"postgresql+psycopg2://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"
	engine = create_engine(engine_str)
	return engine
