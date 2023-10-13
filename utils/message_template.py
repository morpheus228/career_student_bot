import json, os
import jinja2

from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


class MessageTemplateError(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path


class NotDefinedKeyboardType(MessageTemplateError):
    pass


class NotDefinedTemplate(MessageTemplateError):
    pass


class MessageTemplate:
    def __init__(self, text: str, reply_markup: InlineKeyboardMarkup|ReplyKeyboardMarkup):
        self.text: str = text
        self.reply_markup: InlineKeyboardMarkup|ReplyKeyboardMarkup = reply_markup

    @classmethod
    def from_json(cls, path: str):
        text, reply_markup = MessageJSONTemplate.load(path)
        return cls(text, reply_markup)
            
    def render(self, **kwargs):
        return jinja2.Template(self.text).render(**kwargs), self.reply_markup


class MessageJSONTemplate:
    PATH_PREFIX = "messages/"
    PATH_POSTFIX = ".json"

    @classmethod
    def load(cls, path) -> tuple[str|None, InlineKeyboardMarkup|ReplyKeyboardMarkup|None]:
        template: dict = cls.load_template(path)
        text = cls.load_text(template)
        reply_markup = cls.load_reply_markup(template)
        return text, reply_markup
    
    @classmethod
    def load_template(cls, path) -> dict:
        path = cls.PATH_PREFIX + path +  cls.PATH_POSTFIX

        if os.path.exists(path):
            try:
                with open(path, encoding='utf-8') as file:
                    return json.load(file)
            except Exception:
                raise MessageTemplateError(path)
            
        raise NotDefinedTemplate(path)
    
    @staticmethod
    def load_text(template: dict) -> str|None:
        text = template.get('text', None)

        if text is not None:
            return ''.join(text)

    @classmethod
    def load_reply_markup(cls, template: dict) -> InlineKeyboardMarkup|ReplyKeyboardMarkup|None:
        keyboard = template.get('keyboard', None)
        
        if keyboard is not None:
            kwargs = {key: value for key, value in keyboard.items() if key not in ['type', 'keys']}
            keys = keyboard['keys']

            match keyboard['type']:
                case 'inline':
                    return cls.load_inline_keyboard(keys, kwargs)
                case 'reply':
                    return cls.load_reply_keyboard(keys, kwargs)
                case _:
                    raise NotDefinedKeyboardType
                
    @staticmethod
    def load_inline_keyboard(keys, kwargs) -> InlineKeyboardMarkup:
        return InlineKeyboardBuilder(list(map(lambda row: list(map(lambda key: InlineKeyboardButton(**key), row)), keys))).as_markup(**kwargs)
    
    @staticmethod
    def load_reply_keyboard(keys, kwargs) -> ReplyKeyboardMarkup:
        return ReplyKeyboardBuilder(list(map(lambda row: list(map(lambda key: KeyboardButton(**key), row)), keys))).as_markup(**kwargs) 