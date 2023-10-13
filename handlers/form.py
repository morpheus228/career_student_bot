from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from utils.message_template import MessageTemplate

router = Router()


class States(StatesGroup):
    gender = State()
    name = State()
    faculty = State()
    course = State()
    about = State()
    request = State()
    photo = State()