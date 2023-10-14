import asyncio
import logging
from config import Config
from parser.parser import PostsParser
from repositories import Repository, postgres

logging.basicConfig(level=logging.INFO)


async def main():
    config = Config()
    engine = postgres.get_engine(config.postgres)
    repository = Repository(engine)

    parser = PostsParser(repository)



if __name__ == '__main__':
    asyncio.run(main())