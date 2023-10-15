from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from services.service import Service
from aiogram.fsm.state import State, StatesGroup
import ast

from utils.message_template import MessageTemplate

router = Router()


class States(StatesGroup):
    get = State()



@router.message(Command('add_post'))
async def start(message: Message, state: FSMContext):
    print(message.from_user.id)
    if message.from_user.id in [587247376, 5080581642]:
        await message.answer(text="Введи мероприятие")
        await state.set_state(States.get)


@router.message(States.get)
async def start(message: Message, state: FSMContext, service: Service):
    await service.mailing.make(ast.literal_eval(message.text))

