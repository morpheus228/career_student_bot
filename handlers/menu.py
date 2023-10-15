from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message, FSInputFile, PhotoSize, Document, File, InputFile, URLInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.input_media_photo import InputMediaPhoto
from services.interfaces import SelectCD
from services.interfaces.menu import CategoryСhoiceCD
from services.service import Service
from utils.keyboard import select_points

from utils.message_template import MessageTemplate

router = Router()


@router.message(Command('menu'))
async def menu(message: Message, state: FSMContext, service: Service):
    text, reply_markup = MessageTemplate.from_json('menu/categories').render()
    reply_markup = await service.menu.get_categories_keyboard()
    await message.answer(text=text, reply_markup=reply_markup)


@router.callback_query(F.data.contains('choose_category'))
async def choose_category(callback: CallbackQuery, state: FSMContext, service: Service):
    category_id = SelectCD.unpack(callback.data).id
    await state.update_data(category_id=category_id)
    text, reply_markup = MessageTemplate.from_json('menu/tags').render()
    reply_markup = await service.menu.get_tags_keyboard(category_id)
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


@router.callback_query(F.data.contains('choose_category'))
async def menu(callback: CallbackQuery, state: FSMContext, service: Service):
    category_id = SelectCD.unpack(callback.data).id
    await state.update_data(category_id=category_id)
    text, reply_markup = MessageTemplate.from_json('menu/tags').render()
    reply_markup = await service.menu.get_tags_keyboard(category_id)
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


@router.callback_query(SelectCD.filter(F.object_type=='choose_tag'))
async def select_object(callback: CallbackQuery):
    inline_keyboard, action = select_points(callback)

    if action == -1:
        inline_keyboard = inline_keyboard[:-1]
    elif action == 1:
        inline_keyboard.append([InlineKeyboardButton(text="ПОКАЗАТЬ ➡️", callback_data="show_posts")])

    reply_markup = InlineKeyboardBuilder(inline_keyboard).as_markup()
    await callback.message.edit_reply_markup(reply_markup=reply_markup)


@router.callback_query(F.data == 'show_posts')
async def show_posts(callback: CallbackQuery, state: FSMContext, service: Service, bot: Bot):
    tag_ids = await service.menu.get_selected_tags(callback)
    category_id = (await state.get_data())['category_id']
    post_ids = await service.menu.get_post_ids(category_id, tag_ids)

    await state.update_data(post_ids=post_ids)
    await state.update_data(cur_index=-1)

    await show_post(callback, state, service, 1, bot)


@router.callback_query(F.data == 'next_post')
async def show_posts(callback: CallbackQuery, state: FSMContext, service: Service, bot: Bot):
    await show_post(callback, state, service, 1, bot)


@router.callback_query(F.data == 'prev_post')
async def show_posts(callback: CallbackQuery, state: FSMContext, service: Service, bot: Bot):
    await show_post(callback, state, service, -1, bot)


async def show_post(callaback: CallbackQuery, state: FSMContext, service: Service, shift: int, bot: Bot):
    data = await state.get_data()
    cur_index, post_ids = data['cur_index'], data['post_ids']

    cur_index += shift

    try:
        post_id = post_ids[cur_index]
    except Exception:
        await callaback.message.delete()
        return
    
    post = await service.menu.get_post_by_id(post_id)

    text, reply_markup = MessageTemplate.from_json('menu/post').render(post=post)
    reply_markup = get_keyboard(cur_index, len(post_ids))

    if callaback.message.photo is None:

        if post.photo is None:
            await callaback.message.edit_text(text=text, reply_markup=reply_markup)
            
        else:
            photo = URLInputFile(post.photo)
            await callaback.message.answer_photo(photo, caption=text, reply_markup=reply_markup)
            await callaback.message.delete()

    else:
        if post.photo is None:
            await callaback.message.answer(text, reply_markup=reply_markup)
            await callaback.message.delete()
        else:
            photo = URLInputFile(post.photo)
            await callaback.message.answer_photo(photo, caption=text, reply_markup=reply_markup)
            await callaback.message.delete()
    
    await state.update_data(cur_index=cur_index)


def get_keyboard(cur_index, post_ids_len):
    keyboard = [[]]

    if cur_index > 0:
        keyboard[0].append(InlineKeyboardButton(text='⬅️', callback_data="prev_post"))

    if cur_index < post_ids_len - 1:
        keyboard[0].append(InlineKeyboardButton(text='➡️', callback_data="next_post"))

    if len(keyboard[0]) == 0:
        return None
    else:
        return InlineKeyboardBuilder(keyboard).as_markup()
