from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.message_template import MessageTemplate

router = Router()


@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('commands/start').render(first_name=message.from_user.first_name)
    await message.answer(text=text, reply_markup=reply_markup)


@router.callback_query(F.data == 'start')
async def start_button(callback: CallbackQuery, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('mailings/answer').render()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)

