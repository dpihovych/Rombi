import re
from datetime import datetime

import pytz
from aiogram import Router, Bot, F, types
import tzlocal
import string
import random
from aiogram.filters import Command
import config
from config import BOT_TOKEN
from typing import Any, Dict
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
import sqlite3 as sq

router = Router()
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")


class Signup(StatesGroup):
    name = State()
    age = State()
    email = State()


base = sq.connect("Rombi.db")
cur = base.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                username TEXT,
                full_name TEXT,
                name TEXT,
                age TEXT,
                email TEXT,
                date DATETIME
            )""")


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


@router.message(Command("start"))
async def start(message: Message):
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    r = cur.fetchone()
    if not r:
        # =
        # print("successfully added ", message.from_user.id, message.from_user.username, message.from_user.full_name)

        await message.answer("Привіт, я бот! 👋\n"
                             "І я побачив, що тебе немає в базі данних ☹️\n"
                             "тому щоб отримати доступ до інших моїх команди, напиши - /signup")
    else:
        await message.answer("Привіт, я бот! 👋\n"
                             "Для отримання списку команд введи - /help 📋\n"
                             "В мені з'явилося невеличке оновлення! Якщо хочеш подивитися що змінилося напиши - /renewal")


# help
@router.message(Command("help"))
async def help(message: Message):
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    r = cur.fetchone()
    if not r:
        await message.answer(
            "❌ Тобі потрібно зареєструватися в Rombi і тоді тобі стане доступна ця команда! Щоб зареєструатися, напиши /signup")
    else:
        await message.answer(
            "<b>Меню допомоги:</b>\n\n"
            "<b>Команди які я вмію виконувати, для звичайних користувачів:</b>\n"
            "/start - запуск/перезапускбота\n"
            "/help - меню допомоги\n"
            "/info - інформація\n"
            "/password - генерує випадковий пароль, довжина максимум 10 символів\n\n"
            "<b>Команди які я вмію виконувати, для адміністраторів:</b>\n"
            "Скоро з'явиться"
        )


# password
@router.message(Command("password"))
async def password(message: Message):
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    r = cur.fetchone()
    if not r:
        await message.answer(
            "❌ Тобі потрібно зареєструватися в Rombi і тоді тобі стане доступна ця команда! Щоб зареєструатися, напиши /signup")
    else:
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        numbers = string.digits
        symbols = string.punctuation

        Use_for = lower_case + upper_case + numbers + symbols
        lenght_for_password = 10
        password = "".join(random.sample(Use_for, lenght_for_password))
        await message.answer("Твій згенерований пароль: " + password)


# spam
@router.message(Command("spam"))
async def password(message: Message):
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    r = cur.fetchone()
    if not r:
        await message.answer("❌ Тобі потрібно зареєструватися в Rombi і тоді тобі стане доступна ця команда! Щоб "
                             "зареєструатися, напиши /signup")
    else:
        user_id_to_spam = message.text.replace("/spam ", "")
        print("Спамлю успішно!")
        while True:
            if user_id_to_spam == "5197139803":
                await message.answer("Іди в дупу, це мій розробник, його заспамити не можна!")
                break
            await bot.send_message(user_id_to_spam, "Spam 😈😈😈")


@router.message(Command("profile"))
async def profile(message: Message):
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    r = cur.fetchone()
    if not r:
        await message.answer(
            "❌ Тобі потрібно зареєструватися в Rombi і тоді тобі стане доступна ця команда! Щоб зареєструатися, "
            "напиши /signup")
    else:
        user_id_r = cur.execute("SELECT user_id FROM users WHERE user_id=?", (message.from_user.id,))
        user_id = user_id_r.fetchone()[0]
        full_name_r = cur.execute("SELECT full_name FROM users WHERE user_id=?", (message.from_user.id,))
        full_name = full_name_r.fetchone()[0]
        username_r = cur.execute("SELECT username FROM users WHERE user_id=?", (message.from_user.id,))
        username = username_r.fetchone()[0]
        date_r = cur.execute("SELECT date FROM users WHERE user_id=?", (message.from_user.id,))
        date = date_r.fetchone()[0]
        name_r = cur.execute("SELECT name FROM users WHERE user_id=?", (message.from_user.id,))
        name = name_r.fetchone()[0]
        email_r = cur.execute("SELECT email FROM users WHERE user_id=?", (message.from_user.id,))
        email = email_r.fetchone()[0]
        await message.reply(
            f"👤 Твоє ім'я - {name}\n"
            f"📤 Твій email - {email}\n"
            f"🆔 Твій ID - {user_id}\n"
            f"🧑🏻‍💻 Твій псевдонім - @{username}\n"
            f"🪪 Твоє ім'я в Telegram - {full_name}\n"
            f"📆 Дата реєсттрації - {date}\n")


# signup
@router.message(Command("signup"))
async def signup(message: Message, state: FSMContext):
    await state.set_state(Signup.name)
    await message.answer("Як тебе звати?")


@router.message(Signup.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Signup.age)
    await message.answer("Скільки тобі років?")


@router.message(Signup.age)
async def age(message: Message, state: FSMContext):
    if message.text.isdigit() and len(message.text) < 2:
        await state.update_data(age=message.text)
        await state.set_state(Signup.email)
        await message.answer(
            "Яка твоя електронна скринька? Нам потрібно знати твою електронну пошту, щоб в разі чого зв'язатися з тобою")
    else:
        await message.answer("Вкажи число, а не букву/букви")


@router.message(Signup.email)
async def eemail(message: Message, state: FSMContext):
    email = message.text
    if is_valid_email(email):
        await state.update_data(email=message.text)
        await state.set_state(Signup.email)
        data = await state.get_data()
        await show_summary(message=message, data=data)
    else:
        await message.reply("Це недійсна email-адреса")
        await state.set_state(state=None)


# info
@router.message(Command("info"))
async def info(message: Message):
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    r = cur.fetchone()
    if not r:
        await message.answer("❌ Тобі потрібно зареєструватися в Rombi і тоді тобі стане доступна ця команда! Щоб "
                             "зареєструатися, напиши /signup")
    else:
        await message.answer(
            "<b>Інформація:</b> Це бот Ромбі, створенний однією українською людиною, яка до речі проти росії і мені "
            "стало скучно... Ну і я вирішив зробити свого Telegram бота і мені стало весело)). Також я надіюся що бот "
            "буде оновлюватися і далі, тому чекайте версії 3.01. А я піду поїм вареників і буду думати як можна "
            "вдосконалити бота😉\n\n<b>Технічна інформація:</b>\nТех. підтримка: soon\nМови програмування: Python, "
            "Aiogram 3\nВерсія боту: 2.103\n\n<b>Комадна розробки:</b>\nГоловний розробник: @Videodimaa\nДизайнер "
            "аватару: @Videodimaa\nДизайнер/обробник повідомлень: @Videodimaa")


# renewal
@router.message(Command("renewal"))
async def send_welcome(message: Message):
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    r = cur.fetchone()
    if not r:
        await message.answer(
            "❌ Тобі потрібно зареєструватися в Rombi і тоді тобі стане доступна ця команда! Щоб зареєструатися, напиши /signup")
    else:
        await message.reply(
            f"<b>Список оновленнь:</b>\n\n<b>1. Дві нових команди</b><b>ТІЛЬКИ</b><b>для "
            f"адміністраторів</b>\n<code>/channel_id</code> - отримання id каналу\n<code>/id</code> - отримання id "
            f"акаунту\n<code>/ping</code> - можна взнати свій пінг\n<code>/spam</code> - можна надіслати 500 повідомленнь "
            f"користувачу\n<b>Якщо ти хочеш отримтаи звання адміністратора, пиши сюди @Videodimaa </b>\n\n<b>2. Тепер в "
            f"Ромбі підтримує <code>моноширий</code> текст</b>\n\n<b>3. З'явилося 3 нових команди для "
            f"модерації!</b>\n<b>А саме:</b>\n<b><code>/ban</code> - можна заблокувати "
            f"користувача</b>\n<b><code>/mute</code> - можна заборонити писати користувачу "
            f"гоидну</b>\n<b>/<code>unmute</code> - можна дозволити писати користувачу раніше години</b>\n\n<b>4. Тепер у "
            f"Ромбі є РП(можна створити якусь міні гру) команди!</b>\n<b>А саме:</b>\n<b>Вистрілити</b>\n<b>Дати "
            f"пендика</b>\n<b>Дати п'ять</b>\n\nОсь так Ромбі зустрів <b>2023</b> рік!")


# how_admin
@router.message(Command("how_admin"))
async def send_welcome(message: Message):
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    r = cur.fetchone()
    if not r:
        await message.answer(
            "❌ Тобі потрібно зареєструватися в Rombi і тоді тобі стане доступна ця команда! Щоб зареєструатися, напиши /signup")
    else:
        await message.reply(
            f"{message.from_user.full_name}, заповни цю <a href='https://docs.google.com/forms/d"
            f"/1tSjH6Yex9VAHtIZIvcLXJ2frYWNQw7VrouterYrZIPJ5fBI'>форму</a>, і ми приймемо своє рішення😉")


# allcfa
@router.message(Command("cmd"))
async def send_welcome(message: Message):
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    r = cur.fetchone()
    if not r:
        await message.answer(
            "❌ Тобі потрібно зареєструватися в Rombi і тоді тобі стане доступна ця команда! Щоб зареєструатися, напиши /signup")
    else:
        await message.reply(
            "/start\n/help\n/info\n/renewal\n/how_admin\n/id\n/channel_id\n/password\n/issue\n/send\nматюк\nСлово\nокупант\nпутін\nЗеленський\nмосквa\nромбі, що таке coding?\nромбі"
            "Ромбі, ти де?\nромб\nа ти хто?\nхто тут красава?)")


async def show_summary(message: Message, data: Dict[str, Any]):
    name = data["name"]
    age = data["age"]
    data["email"] = message.text
    email = data["email"]
    text = f'{name}, {age}, {email}'
    date = datetime.now(pytz.timezone('Europe/Kiev')).strftime("%d.%m.%Y %H:%M")
    print("Що вказав юзер", text)
    upd_text = f'{message.from_user.id}, {message.from_user.username}, {message.from_user.full_name}'
    print("Що вказав юзер + то, що бот вияснив ", text, upd_text)
    cur.execute('INSERT INTO users (user_id, username, full_name, name, age, email, date)'
                'VALUES (?, ?, ?, ?, ?, ?, ?)',
                (message.from_user.id, message.from_user.username, message.from_user.full_name, name, age, email, date))
    base.commit()
    # await message.answer(text=text)
    await message.answer(
        "🥳 Вітаю! Ти успшіно зареєструвався в Rombi!!!\nДля того щоб подивтися свій обліковий запис, напиши - /profile")
