from .preferences import Preferences
from .menu import Menu
from .mailing import Mailing

from aiogram.filters.callback_data import CallbackData


class SelectCD(CallbackData, prefix="select_object"):
    id: int
    object_type: str
    is_selected: bool


class ChooseCD(CallbackData, prefix="choose_object"):
    id: int