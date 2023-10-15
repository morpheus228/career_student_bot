from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from services.service import Service

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


@router.message(Command('mailing'))
async def mailing(message: Message, state: FSMContext, service: Service):
    if await service.preferences.get_user_mailing_mode(message.from_user.id):
        categories = await service.preferences.get_user_categories(message.from_user.id)
        tags = await service.preferences.get_user_tags(message.from_user.id)  
        text, reply_markup = MessageTemplate.from_json('commands/activated_mailing').render(categories=categories, tags=tags)
        
    else:
        text, reply_markup = MessageTemplate.from_json('commands/deactivated_mailing').render()

    await message.answer(text=text, reply_markup=reply_markup)
