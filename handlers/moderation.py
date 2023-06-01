from aiogram import Router, types, Bot, F, exceptions, filters
from aiogram.filters import Command
import time
from filters.bot_filters import IsChatAdmin
import config
from loguru import logger
from config import permissions, permissions1
from aiogram.types import Message, ChatPermissions
from babel.dates import format_timedelta

from utils.timedelta import parse_timedelta_from_message

router = Router()
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")


# mute
@router.message(Command("ro", prefix="/!."), IsChatAdmin())
async def mute(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповідь на повідомлення")
        return

    duration = await parse_timedelta_from_message(message)
    if not duration:
        return

    try:
        await message.chat.restrict(
            message.reply_to_message.from_user.id, permissions, until_date=duration
        )

        logger.info(
            "User {user} restricted by {admin} for {duration}",
            user=message.reply_to_message.from_user.id,
            admin=message.from_user.id,
            duration=duration,
        )
    except Exception as e:
        logger.error("Failed to restrict chat member: {error!r}", error=e)
        return False

    await message.reply(
        "Ви успішно заборонили писати користувачу @{user}, на: {duration}".format(
            user=message.reply_to_message.from_user.username,  # message.reply_to_message.from_user,
            duration=format_timedelta(
                duration, granularity="seconds", format="short", locale="uk"
            ),
        )
    )

    return True


# unmute
@router.message(Command("unmute", prefix="/!."), IsChatAdmin())
async def delete(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповідь на повідомлення")
        return

    else:
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, permissions1)
        await message.reply("Вітаю! Ви дозволили писати користувачу раніше ніж за годину")
    return


# admin
@router.message(Command("admin", prefix="/!."), IsChatAdmin())
async def cmd_admin(message: types.Message):
    if not message.reply_to_message:
        await bot.promote_chat_member(message.chat.id, config.BOT_OWNER, **config.ADMIN_OWNER)
        return
    else:
        await bot.promote_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id,
                                      **config.ADMIN)

        await message.answer(f"{message.reply_to_message.from_user.id} тепер став адміністраторм! Вітаю!")
        return
