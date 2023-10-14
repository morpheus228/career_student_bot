import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

# from middlewares.user_availability import UserAvailabilityMiddleware

from handlers.commands import router as command_router
from handlers.mailings import router as mailings_router
# from handlers.form import router as form_router

from config import Config
# from repositories import Repository, postgres
# from services import Service


logging.basicConfig(level=logging.INFO)


def register_routers(dp: Dispatcher):
    dp.include_router(command_router)
    dp.include_router(mailings_router)
    # dp.include_router(form_router)
    # dp.include_router(swiping_router)
    

# def register_middlewares(dp: Dispatcher):
#     dp.update.outer_middleware(UserAvailabilityMiddleware(dp['repository'].users))


async def register_default_commands(dp: Dispatcher):
    command_list = []
    for key in dp['commands']:
        command_list.append(BotCommand(command=key[1:], description=dp['commands'][key]))

    await dp['bot'].set_my_commands(command_list)


# def on_first_startup(repository: Repository):
#     from repositories.postgres.models import Base
#     Base.metadata.drop_all(repository.engine)
#     Base.metadata.create_all(repository.engine)


async def main():
    config = Config()
    bot = Bot(config.bot.token, parse_mode='HTML')

    # engine = postgres.get_engine(config.postgres)
    # repository = Repository(engine)
    # service = Service(repository, config, bot)

    dp = Dispatcher(storage=MemoryStorage())
    
    dp['config'] = config
    dp['dp'] = dp
    dp['bot'] = bot
    # dp['service'] = service
    # dp['repository'] = repository

    dp['commands'] = {"/menu": "Главное меню",
                      "/mailing": "Рассылка по интересам"}
    
    # on_first_startup(repository)

    await register_default_commands(dp)
    
    register_routers(dp)
    # register_middlewares(dp)

    await dp.start_polling(dp['bot'])


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
