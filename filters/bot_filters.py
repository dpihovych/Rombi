from typing import Union

from aiogram import Router
from aiogram import Bot, types
from aiogram.client import bot
from aiogram.types import Message

import config
from aiogram.filters import Filter, BaseFilter
from config import BOT_OWNER, ADMINS

router = Router()
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")


class IsChatAdmin(BaseFilter):
    async def __call__(self, mq: Union[Message], bot: Bot) -> bool:
        chat = mq.chat if isinstance(mq, Message) else mq.message.chat
        chat_admins = await bot.get_chat_administrators(chat.id)
        chat_admin_ids = frozenset((member.user.id for member in chat_admins))

        return mq.from_user.id in chat_admin_ids
