from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from services import Service
from services.interfaces import ChooseCD, SelectCD
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.keyboard import select_points
from utils.message_template import MessageTemplate
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.callback_query(F.data == 'mailing_deactivate')
async def mailing_activate(callback: CallbackQuery, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('mailings/deactivated').render()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


@router.callback_query(F.data == 'mailing_cancel')
async def mailing_activate(callback: CallbackQuery, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('mailings/cancel').render()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


@router.callback_query(F.data == 'mailing_activate')
async def mailing_activate(callback: CallbackQuery, state: FSMContext, service: Service):
    text, reply_markup = MessageTemplate.from_json('mailings/ask_categories').render()
    reply_markup = await service.preferences.get_categories_keyboard()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)
    


@router.callback_query(SelectCD.filter(F.object_type=='category'))
async def select_object(callback: CallbackQuery):
    inline_keyboard, action = select_points(callback)

    if action == -1:
        inline_keyboard = inline_keyboard[:-1]
    elif action == 1:
        inline_keyboard.append([InlineKeyboardButton(text="ПОДТВЕРДИТЬ ➡️", callback_data="confirm_categories")])

    reply_markup = InlineKeyboardBuilder(inline_keyboard).as_markup()
    await callback.message.edit_reply_markup(reply_markup=reply_markup)


@router.callback_query(F.data == 'confirm_categories')
async def confirm_categories(callback: CallbackQuery, state: FSMContext, service: Service):
    await service.preferences.set_user_categories(callback.from_user.id, callback)
    text, reply_markup = MessageTemplate.from_json('mailings/ask_tags').render()
    reply_markup = await service.preferences.get_tags_keyboard()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)



@router.callback_query(SelectCD.filter(F.object_type=='tag'))
async def select_object(callback: CallbackQuery):
    inline_keyboard, action = select_points(callback)

    if action == -1:
        inline_keyboard = inline_keyboard[:-1]
    elif action == 1:
        inline_keyboard.append([InlineKeyboardButton(text="ПОДТВЕРДИТЬ ➡️", callback_data="confirm_tags")])

    reply_markup = InlineKeyboardBuilder(inline_keyboard).as_markup()
    await callback.message.edit_reply_markup(reply_markup=reply_markup)


@router.callback_query(F.data == 'confirm_tags')
async def confirm_tags(callback: CallbackQuery, state: FSMContext, service: Service):
    await service.preferences.set_user_tags(callback.from_user.id, callback)
    text, reply_markup = MessageTemplate.from_json('mailings/success').render()
    await callback.message.edit_text(text=text, reply_markup=reply_markup)