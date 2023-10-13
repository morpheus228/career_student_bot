from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass
class BotConfig:
    token: str
    # admin_ids: list


@dataclass
class PostgresConfig:
    host: str
    password: str
    user: str
    database: str
    port: str


@dataclass
class Config:
    bot: BotConfig
    postgres: PostgresConfig

    def __init__(self):
        load_dotenv('.env')
        
        self.bot = BotConfig(
            token=os.getenv("BOT_TOKEN"))
        
        self.postgres = PostgresConfig(
            host=os.getenv('POSTGRES_HOST'),
            password=os.getenv('POSTGRES_PASSWORD'),
            user=os.getenv('POSTGRES_USER'),
            database=os.getenv('POSTGRES_DB'),
            port=os.getenv('POSTGRES_PORT'))