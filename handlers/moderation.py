from aiogram import Router, types, Bot, F
from aiogram.filters import Command
import time
from filters.bot_filters import IsChatAdmin
import config
from config import permissions, permissions1
from aiogram.types import Message, ChatPermissions

router = Router()
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")


# mute
@router.message(Command("mute"), IsChatAdmin())
async def mute(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповідь на повідомлення")
        return

    if message.reply_to_message:
        if F.text.containts('1d'):
            oneday = 86400
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, permissions,
                                       until_date=oneday)
        await message.reply(f"Вітаю! Ви заборонили користувачу писати на один день!")
        if F.text.containts('2d'):
            twodays = 172800
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, permissions,
                                       until_date=twodays)
        await message.reply(f"Вітаю! Ви заборонили користувачу писати на один день!")
        if F.text.containts('1w'):
            oneweek = 604800
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, permissions,
                                       until_date=oneweek)
        await message.reply(f"Вітаю! Ви заборонили користувачу писати на один день!")
        if F.text.containts('2w'):
            twoweeks = 1209600
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, permissions,
                                       until_date=twoweeks)
        await message.reply(f"Вітаю! Ви заборонили користувачу писати на один день!")
    return


# unmute
@router.message(Command("unmute"), IsChatAdmin())
async def delete(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповідь на повідомлення")
        return

    else:
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, permissions1)
        await message.reply("Вітаю! Ви дозволили писати користувачу раніше ніж за годину")
    return


# ban
@router.message(Command("ban"), IsChatAdmin())
async def delete(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповідь на повідомлення")

    else:
        to_ban_time = int(time.mktime(message.date.timetuple())) + 604800000
        await message.reply(
            f"Вітаю! Ви успішно заблокували <b>{message.reply_to_message.from_user.full_name}</b>? на цілий тиждень!")
        await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=to_ban_time)


# admin
@router.message(Command("admin"), IsChatAdmin())
async def cmd_admin(message: types.Message):
    if not message.reply_to_message:
        await bot.promote_chat_member(message.chat.id, config.BOT_OWNER, **config.ADMIN_OWNER)
        return
    else:
        await bot.promote_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id,
                                      **config.ADMIN)

        await message.answer(f"{message.reply_to_message.from_user.id} тепер став адміністраторм! Вітаю!")
        return
