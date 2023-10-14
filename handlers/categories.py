from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.message_template import MessageTemplate

router = Router()

@router.callback_query(F.data == 'olymp')
async def olymp(callback: CallbackQuery, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('categories/olymp').render()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


@router.callback_query(F.data == 'forum')
async def forum(callback: CallbackQuery, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('categories/forum').render()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


@router.callback_query(F.data == 'intern')
async def intern(callback: CallbackQuery, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('categories/intern').render()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


@router.callback_query(F.data == 'test')
async def test(callback: CallbackQuery, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('categories/test').render()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)
