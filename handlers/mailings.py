from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.message_template import MessageTemplate

router = Router()

@router.callback_query(F.data == 'mailing_cancel')
async def mailing_activate(callback: CallbackQuery, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('mailings/cancel').render()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


@router.callback_query(F.data == 'mailing_activate')
async def mailing_activate(callback: CallbackQuery, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('mailings/ask_categories').render()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)

