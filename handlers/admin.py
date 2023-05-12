from aiogram import types, Bot
import logging
from time import sleep
from config import ADMIN, BOT_OWNER, ADMIN_OWNER, BOT_TOKEN
from filters.bot_filters import IsChatAdmin
import re
from pyspeedtest import SpeedTest
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
import config
from pyspeedtest import SpeedTest

st = SpeedTest()
router = Router()
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")


# ping pong
@router.message(Command("ping"))
async def ping_pong(message: types.Message):
    bot_msg = await message.answer(f'Pong')
    await bot.send_chat_action(message.chat.id, 'typing')
    ping = st.ping()
    bot_msg = await bot_msg.edit_text(f'Твій пінг {ping:.1f}мс')


@router.message(Command("channel_id"), IsChatAdmin())
async def yes_send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, f"ID цього чату: {message.chat.id}")


@router.message(Command("channel_id"))
async def not_send_welcome(message: types.Message):
    await message.reply(f"Ти не є в списку адмінів!")


@router.message(Command('id'))
async def yes_id(message: types.Message):
    await message.reply(f"Твій ID: {message.from_user.id}")
